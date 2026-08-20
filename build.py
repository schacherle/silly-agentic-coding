#!/usr/bin/env python3
"""
Compiles modular agent prompts into monolithic files.
This script reads template files from `agent_sources/templates/` and injects
common shared blocks from `agent_sources/common/` to produce the final
compiled agent markdown files in the `agents/` directory.
"""

import os
import sys
import argparse


COMMON_FILES: dict[str, str] = {
    "COMMON_PRIME_DIRECTIVE": "prime_directive.md",
    "COMMON_TONE_RULES": "tone_rules.md",
    "COMMON_JOURNAL_RULES": "journal_rules.md",
    "COMMON_SECURITY_RULES": "security_rules.md",
    "COMMON_PR_GATE": "pr_gate.md",
    "COMMON_SAMPLE_COMMANDS": "sample_commands.md",
    "COMMON_VERIFICATION_RULE": "verification_rule.md",
}


def load_common_blocks(common_dir: str) -> dict[str, str]:
    """Load and return all common block contents keyed by placeholder name."""
    common_blocks: dict[str, str] = {}
    for key, filename in COMMON_FILES.items():
        filepath = os.path.join(common_dir, filename)
        if not os.path.exists(filepath):
            print(
                f"Error: Required common component {filename} not found at {filepath}",
                file=sys.stderr,
            )
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as f:
            common_blocks[key] = f.read().strip()
    return common_blocks


def render_blocks_for_agent(
    common_blocks: dict[str, str], agent_name: str
) -> dict[str, str]:
    """Render common blocks with agent-specific name substitutions."""
    rendered: dict[str, str] = {}
    for key, raw_text in common_blocks.items():
        text = raw_text.replace("{{AGENT_NAME_UPPER}}", agent_name.upper())
        text = text.replace("{{AGENT_NAME_LOWER}}", agent_name.lower())
        text = text.replace("{{AGENT_NAME}}", agent_name.capitalize())
        rendered[key] = text
    return rendered


def compile_template(content: str, rendered_blocks: dict[str, str]) -> str:
    """Replace all placeholders in a template with rendered common blocks."""
    compiled = content
    for placeholder, replacement in rendered_blocks.items():
        compiled = compiled.replace(f"{{{{{placeholder}}}}}", replacement)
    return compiled


def check_output(output_path: str, compiled_content: str, template_name: str) -> bool:
    """Return True if the output file matches the compiled content."""
    if not os.path.exists(output_path):
        print(f"Check failed: {output_path} is missing.")
        return False
    with open(output_path, "r", encoding="utf-8") as out_f:
        existing_content = out_f.read()
    if existing_content != compiled_content:
        print(f"Check failed: {template_name} is out-of-sync.")
        return False
    return True


def process_templates(
    templates_dir: str,
    output_dir: str,
    common_blocks: dict[str, str],
    check: bool,
    display_output_dir: str = "agents",
) -> list[str]:
    """Process all templates and return a list of any out-of-sync template names."""
    if not os.path.exists(templates_dir):
        print(f"Warning: Templates directory {templates_dir} does not exist.", file=sys.stderr)
        return []

    templates = sorted(f for f in os.listdir(templates_dir) if f.endswith(".md"))
    if not templates:
        print(f"Warning: No templates found in {templates_dir}.", file=sys.stderr)
        return []

    os.makedirs(output_dir, exist_ok=True)
    out_of_sync: list[str] = []

    for template_name in templates:
        template_path = os.path.join(templates_dir, template_name)
        output_path = os.path.join(output_dir, template_name)

        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        agent_name = os.path.splitext(template_name)[0]
        rendered_blocks = render_blocks_for_agent(common_blocks, agent_name)
        compiled_content = compile_template(content, rendered_blocks)

        if check:
            if not check_output(output_path, compiled_content, f"{display_output_dir}/{template_name}"):
                out_of_sync.append(f"{display_output_dir}/{template_name}")
        else:
            with open(output_path, "w", encoding="utf-8") as out_f:
                out_f.write(compiled_content)
            print(f"Compiled: {template_name} -> {display_output_dir}/{template_name}")

    return out_of_sync


def main() -> None:
    """
    Parse command-line arguments and execute the compilation process.

    If ``--check`` is provided, verifies that output files match the expected
    compiled output without writing to disk. Otherwise, generates or overwrites
    compiled files in the ``agents/`` and ``agents_bulk/`` directories.
    """
    parser = argparse.ArgumentParser(
        description="Compile modular agent prompts into monolithic files."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if generated agents are up-to-date without writing changes.",
    )
    args = parser.parse_args()

    project_root = os.path.dirname(os.path.abspath(__file__))
    sources_dir = os.path.join(project_root, "agent_sources")
    common_dir = os.path.join(sources_dir, "common")

    if not os.path.exists(common_dir):
        print(f"Error: Common directory not found at {common_dir}", file=sys.stderr)
        sys.exit(1)

    common_blocks = load_common_blocks(common_dir)

    target_configs = [
        {
            "name": "Standard Agents",
            "templates_dir": os.path.join(sources_dir, "templates"),
            "output_dir": os.path.join(project_root, "agents"),
            "display_output_dir": "agents",
        },
        {
            "name": "Bulk Refactoring Agents",
            "templates_dir": os.path.join(sources_dir, "bulk_templates"),
            "output_dir": os.path.join(project_root, "agents_bulk"),
            "display_output_dir": "agents_bulk",
        },
    ]

    all_out_of_sync: list[str] = []

    for target in target_configs:
        templates_dir = target["templates_dir"]
        output_dir = target["output_dir"]
        display_dir = target["display_output_dir"]

        if not os.path.exists(templates_dir):
            if args.check:
                print(f"Check failed: {templates_dir} does not exist.")
                all_out_of_sync.append(templates_dir)
            continue

        out_of_sync = process_templates(
            templates_dir,
            output_dir,
            common_blocks,
            args.check,
            display_output_dir=display_dir,
        )
        all_out_of_sync.extend(out_of_sync)

    if args.check:
        if all_out_of_sync:
            print(
                "\nError: Some agent prompts are out-of-sync. "
                "Please run 'python3 build.py' to compile changes.",
                file=sys.stderr,
            )
            sys.exit(1)
        else:
            print("Check passed: All generated agents are up-to-date.")
            sys.exit(0)
    else:
        print("\nAll agent prompts compiled successfully.")


if __name__ == "__main__":
    main()


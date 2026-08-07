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

def main():
    """
    Parses command-line arguments and executes the compilation process.
    If `--check` is provided, it verifies that the output files match the
    expected compiled output without writing to the disk. Otherwise, it
    generates or overwrites the compiled files in the `agents/` directory.
    """
    parser = argparse.ArgumentParser(description="Compile modular agent prompts into monolithic files.")
    parser.add_argument("--check", action="store_true", help="Check if generated agents are up-to-date without writing changes.")
    args = parser.parse_args()

    project_root = os.path.dirname(os.path.abspath(__file__))
    sources_dir = os.path.join(project_root, "agent_sources")
    common_dir = os.path.join(sources_dir, "common")
    templates_dir = os.path.join(sources_dir, "templates")
    output_dir = os.path.join(project_root, "agents")

    # Verify paths
    for path, name in [(common_dir, "Common directory"), (templates_dir, "Templates directory")]:
        if not os.path.exists(path):
            print(f"Error: {name} not found at {path}", file=sys.stderr)
            sys.exit(1)

    # Load common blocks
    common_blocks = {}
    common_files = {
        "COMMON_PRIME_DIRECTIVE": "prime_directive.md",
        "COMMON_TONE_RULES": "tone_rules.md",
        "COMMON_JOURNAL_RULES": "journal_rules.md",
        "COMMON_SECURITY_RULES": "security_rules.md",
        "COMMON_PR_GATE": "pr_gate.md",
        "COMMON_SAMPLE_COMMANDS": "sample_commands.md"
    }

    for key, filename in common_files.items():
        filepath = os.path.join(common_dir, filename)
        if not os.path.exists(filepath):
            print(f"Error: Required common component {filename} not found at {filepath}", file=sys.stderr)
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as f:
            common_blocks[key] = f.read().strip()

    # Get templates
    templates = [f for f in os.listdir(templates_dir) if f.endswith(".md")]
    if not templates:
        print("Warning: No templates found in templates directory.", file=sys.stderr)
        sys.exit(0)

    os.makedirs(output_dir, exist_ok=True)
    out_of_sync = []

    for template_name in sorted(templates):
        template_path = os.path.join(templates_dir, template_name)
        output_path = os.path.join(output_dir, template_name)

        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract agent name from filename (e.g. "architect.md" -> "architect")
        agent_name = os.path.splitext(template_name)[0]
        agent_name_upper = agent_name.upper()
        agent_name_lower = agent_name.lower()
        agent_name_title = agent_name.capitalize()

        # Render common blocks with agent name replacements
        rendered_blocks = {}
        for key, raw_text in common_blocks.items():
            rendered = raw_text.replace("{{AGENT_NAME_UPPER}}", agent_name_upper)
            rendered = rendered.replace("{{AGENT_NAME_LOWER}}", agent_name_lower)
            rendered = rendered.replace("{{AGENT_NAME}}", agent_name_title)
            rendered_blocks[key] = rendered

        # Replace placeholders in template
        compiled_content = content
        for placeholder, replacement in rendered_blocks.items():
            compiled_content = compiled_content.replace(f"{{{{{placeholder}}}}}", replacement)

        # Check or write
        if args.check:
            if not os.path.exists(output_path):
                print(f"Check failed: {output_path} is missing.")
                out_of_sync.append(template_name)
            else:
                with open(output_path, "r", encoding="utf-8") as out_f:
                    existing_content = out_f.read()
                if existing_content != compiled_content:
                    print(f"Check failed: {template_name} is out-of-sync.")
                    out_of_sync.append(template_name)
        else:
            with open(output_path, "w", encoding="utf-8") as out_f:
                out_f.write(compiled_content)
            print(f"Compiled: {template_name} -> agents/{template_name}")

    if args.check:
        if out_of_sync:
            print("\nError: Some agent prompts are out-of-sync. Please run 'python3 build.py' to compile changes.", file=sys.stderr)
            sys.exit(1)
        else:
            print("Check passed: All generated agents are up-to-date.")
            sys.exit(0)
    else:
        print("\nAll agent prompts compiled successfully.")

if __name__ == "__main__":
    main()

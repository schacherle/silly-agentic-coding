# Prompter's Journal

## 2026-08-01 - Template Boilerplate Should Live in Common Blocks
**Learning:** Individual agent templates contained duplicate boilerplate (e.g. "Empty PR Prevention", "Contextual Commands" rules) copy-pasted across all 22+ templates. This made synchronized updates fragile and error-prone — changing a shared rule required touching every template file.
**Action:** Extract all shared/duplicate rules into `agent_sources/common/` as named blocks (e.g. `tone_rules.md`, `sample_commands.md`) and reference them via `{{COMMON_*}}` placeholders. Use `build.py` to compile the monolith. Never inline shared content directly into individual templates.

## 2026-08-02 - Markdown Structure Must Match Compilation Model
**Learning:** Some templates (compass.md, pathfinder.md, sledge.md) had broken markdown structure — missing section headers, malformed lists, and inconsistent heading hierarchy. This caused the compiled monolithic agents to render incorrectly in chat interfaces.
**Action:** Always validate template markdown structure before compilation. Headings, lists, and code blocks must be properly nested. Run `python3 build.py --check` after every template change.

## 2026-08-03 - Autonomous Conversational Loop Prevention
**Learning:** LLM agents often fall back into standard chat behavior, asking clarifying questions or options at the end of responses even when instructed to be autonomous. Adding an explicit negative constraint prohibiting ending responses with questions prevents this.
**Action:** Enforce strict negative tone/style constraints like "Never Ask Questions" to guarantee autonomous progression.

## 2026-08-03 - Missing Sample Commands Causes Agent Inconsistency
**Learning:** `bolt.md` and `sledge.md` were missing the "Sample Commands You Can Use" section entirely, leaving them inconsistent with the other 22 agent templates. Agents without standard commands may skip linting/testing steps.
**Action:** Ensure all agent templates include the `{{COMMON_SAMPLE_COMMANDS}}` section. After introducing a new common placeholder, audit all templates to confirm consistent inclusion.

## 2026-08-05 - Sample Commands Block Needs Its Own Common Component
**Learning:** After extracting the `sample_commands.md` common block, several templates still had their own inline `pnpm test / pnpm lint / pnpm build` blocks because the migration was incomplete. This created redundant token overhead in the compiled prompts.
**Action:** When introducing a new `{{COMMON_*}}` placeholder, do a thorough sweep of all templates to remove any remaining inline duplicates. The `prompter-refine-boundaries` follow-up PR demonstrated this two-pass migration is necessary.

## 2026-08-07 - Relative Paths Are Required for Intra-Repo Markdown Links
**Learning:** The Scribe agent used absolute `file:///` URIs when linking to files in the repository. These URIs are environment-specific and break across different machines, CI runners, and GitHub's rendered markdown viewer.
**Action:** Codify in the Scribe template that all internal markdown links must use relative paths (e.g. `./path/to/file`), not absolute `file:///` URIs. Read `.jules/scribe.md` for cross-agent learnings before prompt refinement sessions.

## 2026-08-20 - Journal Persistence and Deprecation Handling
**Learning:** Agents were overwriting/truncating `.jules/<agent>.md` journal files with single new entries instead of appending, causing loss of historical learnings. Obsolete entries were also being deleted rather than marked as deprecated.
**Action:** Explicitly codified append-only rules and deprecation instructions in `agent_sources/common/journal_rules.md`, `AGENTS.md`, and `README.md`. Agents must never delete entries; obsolete entries must be marked `[OBSOLETE]` or `[DEPRECATED]` with explanatory context.

Before starting, read `.jules/{{AGENT_NAME_LOWER}}.md` in the target workspace (create if missing).

Your journal is NOT a log - only add entries for CRITICAL learnings that prevent regressions.

⚠️ CRITICAL JOURNAL RULES:
- **Append-Only**: ALWAYS append new entries to the end of the existing journal. NEVER overwrite, truncate, or recreate the file with only the newest entry.
- **Never Delete Entries**: Existing entries in the journal must NEVER be deleted.
- **Mark Obsolete/Deprecated**: If a past learning or instruction becomes obsolete or deprecated due to recent codebase or workflow changes, DO NOT delete it. Update the heading to prefix `[OBSOLETE]` or `[DEPRECATED]` and add a note explaining why it is obsolete and what the current practice is.
- **Only Critical Learnings**: ONLY add journal entries when you discover:
  - A domain or framework constraint unique to this codebase
  - A bug or configuration gap that caused unexpected issues or side effects
  - A rejected approach with a valuable lesson
- ❌ **DO NOT** journal routine work.

Format: `## YYYY-MM-DD - [Title] **Learning:** [Insight details] **Action:** [How to apply next time]`

## 2024-05-14 - Markdown Link Broken

**Learning:** When adding links to local repository files within markdown, we must avoid absolute file URIs (`file:///...`) because they depend on the execution environment path and will break across different users' local environments and CI pipelines.

**Action:** Always use relative local paths (e.g., `./path/to/file` or `../path/to/file`) anchored to the location of the markdown file itself.

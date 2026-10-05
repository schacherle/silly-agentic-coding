# Archivist's Journal

## 2026-10-05 - Jules Environment & Archival Data Boundaries

**Learning:** When executing inside Jules (cloud git-repository environment), the gigabyte-scale image scans (`exports/`) and the Gemini Multimodal Vision API key (`gemini-key`) are intentionally excluded via `.gitignore`. The transcription engine (`transcribe_matriken.py`) runs out-of-band locally, producing versioned artifacts (`matriken/<parish>/<buch>/kandidaten_namen.jsonl`, `transkriptionen.csv`, `transkriptionen.md`, `extrakt.txt`).

**Action:** Archivist's scope in Jules is strictly focused on repository-internal operations:
1. Curating candidate surnames from `kandidaten_namen.jsonl` into `namen.txt`.
2. Modeling verified families, vital events, and SOA Třeboň archival citations into `scripts/build_gedcom.py`.
3. Standardizing locations via CompGen GOV identifiers (`GOV_PLACES`).
4. Regenerating and validating `trees/schacherl_stammbaum.ged` using `python3 scripts/build_gedcom.py` (which requires only standard library modules: `pathlib`, `datetime`, `re`).

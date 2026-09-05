---
name: akb-new-article
description: Create a new TCAT Assistant Knowledge Base article with schema-compliant metadata and a durable UUIDv4
argument-hint: "Proposed article slug or title"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Create an AKB article

Use for a new page under `docs/assistant/`.

1. Read `docs/assistant/schema.md` and `templates/assistant/article.md` fresh.
2. Choose the location: `concept/` for explanatory knowledge, `workflow/` for a discrete procedure, or the topic `index.md` only for policy.
3. Create the page with every required frontmatter field and the nine required headings from the schema.
4. Generate a new UID from the repository root; never copy or derive one:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    python utilities/akb_generate_uid.py
    ```

    Alternatively use `python utilities/akb_generate_uid.py --file <path>`.

5. Preserve the UID on later edits, moves, and renames. For a true deletion, add it to `utilities/akb-retired-uuids.txt`.
6. Validate and regenerate the registry:

    ```powershell
    python utilities/akb_backfill_uids.py --validate
    python utilities/akb_generate_dispatch.py
    ```

## Completion checks

Confirm the UID is a unique canonical lowercase hyphenated UUIDv4 and not retired; `slug` matches the filename; `doc_type` matches the location; fields/headings/status are valid; and dispatch was regenerated, never hand-edited.

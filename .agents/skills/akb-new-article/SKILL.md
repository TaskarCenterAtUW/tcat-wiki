---
name: akb-new-article
description: Create a new TCAT Assistant Knowledge Base article with schema-compliant metadata and a durable UUIDv4
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Create a new Assistant Knowledge Base article

Use this skill when creating a new page under `docs/assistant/`.

## Required workflow

1. Read `docs/assistant/schema.md` and `templates/assistant/article.md` before writing.
2. Choose the correct topic and location:
    - `concept/` for explanatory knowledge.
    - `workflow/` for a procedure with a discrete outcome.
    - The topic's `index.md` only for policy content.
3. Create the page with all required frontmatter fields and the nine required headings.
4. Generate a durable UID from the repository root:

    ```powershell
    .\.venv\Scripts\Activate.ps1
    python utilities/akb_generate_uid.py
    ```

    Insert the printed value as the page's `uid`, or use the file mode to insert it:

    ```powershell
    python utilities/akb_generate_uid.py --file <path-to-new-page.md>
    ```

5. Never copy a UID from another page. Do not derive it from the path, title, or content.
6. Preserve the UID for all later edits, moves, renames, and rewrites.
7. If a page is truly deleted, add its UID to `utilities/akb-retired-uuids.txt` before merging the deletion.
8. Validate and regenerate the registry:

    ```powershell
    python utilities/akb_backfill_uids.py --validate
    python utilities/akb_generate_dispatch.py
    ```

## Completion checklist

- `uid` is a canonical lowercase, hyphenated UUIDv4.
- The UID is unique and absent from `utilities/akb-retired-uuids.txt`.
- `slug` matches the filename and `doc_type` matches the location.
- All required frontmatter fields and headings are present.
- `publication_status` is appropriate for the page's review state.
- Dispatch has been regenerated and was not edited manually.

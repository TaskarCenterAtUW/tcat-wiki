---
name: akb-ingest-transcript
description: Ingest a meeting transcript and propose or apply evidence-grounded Assistant Knowledge Base article changes
argument-hint: "Repo-relative path to a .txt WebVTT transcript"
user-invocable: true
disable-model-invocation: false
---

<!-- @format -->

# Ingest a transcript into the AKB

Process `$args` as evidence, not permission to invent or publish. Require an existing `.txt` WebVTT transcript under `local-storage/transcripts/` unless the user explicitly supplies another valid location. Resolve paths from the repository root (`zensical.toml`).

## Analysis phase

1. Do not edit files, run unrelated utilities/builds/link checks, or commit. Validate the path, then run from the root:

    ```powershell
    python utilities/akb_compress_transcript.py <absolute-transcript-path>
    ```

    Read the generated sibling `.compressed.txt`; do not edit or commit it.

2. Read `docs/assistant/schema.md` and `docs/assistant/dispatch.md` fresh on every invocation. Use the schema as authoritative and dispatch as the current inventory.
3. Extract only reusable definitions, corrections, constraints, decisions, procedures, prerequisites, limitations, and unresolved follow-ups. Ignore greetings, logistics, screen-sharing narration, unsupported speculation, and already-covered material.
4. For each candidate determine: faithful evidence, topic, `concept`/`workflow`/topic-level `policy`, disposition (new/update/no change), confidence/contradictions, and smallest nonduplicative scope.
5. Use existing dispatch paths/statuses. Do not invent links or duplicate articles. Preserve existing UIDs; generate a new canonical UUIDv4 for new articles. If approved deletion occurs, add the old UID to `utilities/akb-retired-uuids.txt`.

Present exactly:

```text
### Proposed changes from `<transcript filename>`

**Evidence notes**
- <uncertainty, contradiction, or context>
- None.

**1. New articles**
- `docs/assistant/<topic>/<type>/<slug>.md` — <evidence-grounded scope>
- None.

**2. Updates**
- `docs/assistant/<topic>/<type>/<slug>.md` — <evidence and affected sections>
- None.
```

End with: **Do you want to make any changes to this plan, or should I proceed with the edits?** Do not claim changes before explicit approval. Use standard characters, including `'` rather than typographic apostrophes.

## Approved edit phase

Only after approval, reread each target and apply transcript-supported changes only. Flag conflicts instead of choosing silently.

For new pages, invoke the `akb-new-article` skill.

For updates, modify only evidence-affected sections/metadata. Regenerate `docs/assistant/dispatch.md` with `python utilities/akb_generate_dispatch.py`; never edit it manually. Validate paths, types, fields, enums, headings, existing links, uncertainty, claims, and publication restrictions. Report changed files, unresolved evidence, and validation performed; run no unrelated work.

## Source-of-truth rules

The schema overrides this skill. Only published pages outside `assistant/support/` enter the human HTML layer; all assistant pages remain raw Markdown in the agent layer. Published pages must not link to stubs, drafts, archived pages, or `assistant/support/` pages.

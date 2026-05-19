---
title: RAG corpus (specification)
---

# RAG corpus (specification)

## Short Answer

This `docs/rag/` section is the **canonical specification** for turning TCAT Wiki assistant pages into retrieval-ready text: what metadata means, how pages should be written, and how exports are produced. Embeddings and vector databases are intentionally out of scope for the base repository.

## Significance

Without a single spec, every consumer reinvents chunking, loses governance fields, or drifts from the public wiki’s meaning.

## What This Means

- Authoritative assistant prose and metadata live under [`docs/assistant/`](../assistant/index.md).
- [Schema reference](schema.md) documents frontmatter and required section headings for assistant pages.
- [`scripts/export_rag.py`](../../scripts/export_rag.py) (repository root) walks `docs/assistant/` and emits JSONL for downstream pipelines.

## What This Does Not Mean

- Not a hosted search service.
- Not an OpenAI or vendor integration.

## Zensical build and link validation

`zensical build` with `[project.validation]` enabled may report a large number of **unresolved link reference** warnings for `docs/assistant/` pages. Common causes:

- `related_pages` entries that use bare slugs (for example `workspace-sandbox`) instead of paths relative to `docs/`
- Empty YAML lists such as `related_pages: []` or `do_not_claim: []` that the validator treats like link targets
- Scaffold pages with `TODO` bodies and incomplete **Related Concepts** sections

**Maintainer expectation:** the wiki repo manager (or a follow-up PR) should resolve these warnings by normalizing `related_pages` paths, adjusting frontmatter so metadata is not parsed as links, and replacing TODO placeholders with valid relative links as content is reviewed. This assistant KB PR intentionally lands structure and RAG export tooling first; link cleanup is not a blocker for merging the corpus layout.

## How To Use This

1. Read [schema.md](schema.md).
2. Author or review pages in `docs/assistant/` using the template.
3. Run `python scripts/export_rag.py` from the repository root (after installing project dependencies).
4. Ingest JSONL in your own indexing environment; replace the `PLACEHOLDER_SITE_URL` prefix on `source_url` values with the published site root (see `site_url` in `zensical.toml`).

## Example

A civic chatbot vendor ingests exported JSONL, replaces the `PLACEHOLDER_SITE_URL` prefix on `source_url` with the public GitHub Pages base, and stores chunks with metadata filters for `risk_level: high`.

## Assistant Guidance

Point technical integrators here instead of summarizing schema from memory.

## Related Concepts

- [Assistant Knowledge Base](../assistant/index.md)
- [Schema reference](schema.md)

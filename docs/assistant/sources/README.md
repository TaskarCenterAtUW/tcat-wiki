---
title: Assistant authoring sources
---

# Assistant authoring sources

Place **raw source material** here for human-and-agent authoring of assistant pages. These files are inputs only; RAG exports read from `docs/assistant/` pages, not from this folder unless content is merged into a page.

## Workspaces workshop transcripts

Workshop recordings (WebVTT):

| Part | File |
|------|------|
| 1 (2026-05-12) | `workspaces-workshop/GMT20260512-OH_Workspaces1_Recording.transcript.vtt` |
| 2 (2026-05-19) | `workspaces-workshop/GMT20260519-OH_Workspaces2_Recording.transcript.vtt` |

If transcripts contain names, credentials, or unreleased URLs you do not want in git, add `docs/assistant/sources/workspaces-workshop/*.vtt` to `.gitignore` and keep them local only during authoring.

## Usage

See [Workspaces transcript authoring queue](../backlog/workspaces-transcript-authoring.md) for the review-and-commit loop.

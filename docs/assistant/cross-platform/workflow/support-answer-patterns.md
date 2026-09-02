---
uid: d5a8cd56-f0c9-4fbd-9c39-41f21c69f7ce
title: Support answer patterns
slug: support-answer-patterns
doc_type: workflow
questions:
    - What patterns should support answers follow?
audiences:
    - planner
    - jurisdiction
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - support
    - helpline
    - communication
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-18
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - These patterns authorize legal conclusions or guaranteed timelines without verification.
related_pages:
    - assistant/support/index.md
    - assistant/intents/support-intents.md
tags:
    - Assistant
---

<!-- @format -->

# Support answer patterns

## Short Answer

Five reusable response structures for helpline and Question Board replies. Pair them with factual pages under `docs/assistant/{topic}/concept/` and `docs/assistant/{topic}/workflow/`, and with [support intents](../../intents.md), so staff retrieve both **what to say** and **how to say it**.

## Significance

Operational questions need consistent tone, explicit uncertainty, and clear next steps. Patterns reduce over-promising and help RAG systems return structured drafts instead of unstructured prose.

## What This Means

| Pattern ID                          | When to use                                                   | Structure                                                                                    |
| :---------------------------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------------- |
| `answer-known-operational`          | Answer is verified                                            | Direct answer → brief explanation → link if needed → next step                               |
| `answer-when-uncertain`             | Needs internal verification                                   | What is known → what is not confirmed → who is checking → interim guidance                   |
| `respond-to-data-error`             | User reports a suspected error                                | Thank them → issue category → reporting path → review lifecycle → agency-scale follow-up     |
| `report-reproducible-product-issue` | User reports a reproducible app or web problem                | Gather context → reproduce → capture evidence → route to support → avoid release promises    |
| `explain-tool-without-overselling`  | Mentioning Walksheds, AccessMap, Mappy Hours, Tasking Manager | Connect to use case → what it does → limitations → next step                                 |
| `reconnect-prior-collaborator`      | Long-running relationship                                     | Acknowledge prior context → current update → answer today's question → concrete continuation |

## What This Does Not Mean

- Not scripts to send verbatim without local edits.
- Not replacements for jurisdiction-specific legal or procurement advice.

## How To Use This

1. Classify the partner message (data error, download help, ecosystem confusion, etc.).
2. Pick the matching intent from [Support intents](../../intents.md).
3. Retrieve factual bullets from the linked question page(s).
4. Apply the pattern structure when drafting email or chat.

For a new reproducible product issue thread, include the current help desk address and relevant staff as instructed. Record the product, platform, device, version, workspace or dataset, steps, expected result, observed result, and available screenshots or identifiers; keep subsequent replies in the existing thread.

## Example

A county asks how long a viewer-reported fix takes. Use **`answer-when-uncertain`** if release timing is unknown: state the public release model, note that timelines vary by validation queue, name who will confirm, and link [How long do corrections take to appear in a public release?](../../os-connect/concept/update-cadence.md).

A user reports that a numeric value is flagged but still submitted. Use **`report-reproducible-product-issue`**: collect the app version and platform, reproduce the behavior, attach evidence, and avoid promising a fix date.

## Assistant Guidance

When generating drafts, label which pattern was applied. If `publication_status: draft` sources are retrieved, disclose that wording is not yet organizationally reviewed.

## Related Concepts

- [Support intents](../../intents.md)

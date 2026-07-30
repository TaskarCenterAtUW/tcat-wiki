---
title: What syntax does an AVIV ScoutRoute quest query use?
slug: quest-definition-query-syntax
doc_type: concept
questions:
    - What syntax does an AVIV ScoutRoute quest query use?
    - How do I write a quest_query for AVIV ScoutRoute?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - formats
    - editing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AVIV ScoutRoute quest_query syntax is identical to every Overpass query feature.
        - A query matches an element when its tags do not satisfy the query.
related_pages:
    - quest-definition-element-targeting.md
    - ../workflow/update-quest-definition-in-workspace.md
    - ../../../aviv-scoutroute/quests/element-query.md
tags:
    - Assistant
---

<!-- @format -->

# What syntax does an AVIV ScoutRoute quest query use?

## Short Answer

The `quest_query` in a Long Form Quest Definition uses a documented tag-filter syntax similar to Overpass, with support for element types, tag presence, exact and regular-expression values, comparisons, dates, and logical expressions.

## Significance

The query determines which mapped elements receive a quest, so an incorrect expression can target too many, too few, or unrelated features.

## What This Means

Examples include `ways`, `shop`, `!shop`, `shop = car`, `shop ~ car|boat`, numeric or date comparisons, `and`, `or`, and parentheses. Regexes match the whole string according to the current guide.

## What This Does Not Mean

The documented similarity to Overpass does not establish that every Overpass feature or execution environment is supported.

## How To Use This

Start with the element type and add the narrowest tag filters needed. Test expressions against workspace data before applying the definition.

## Example

`ways with (footway=sidewalk and !surface)` targets sidewalk ways without a `surface` tag.

## Assistant Guidance

Ask for the exact query, target element type, and intended tags. Cite the current developer guide and avoid silently rewriting ambiguous expressions.

## Related Concepts

- [How do quest definitions target element types?](quest-definition-element-targeting.md)
- [How is a quest definition applied?](quest-definition-application.md)

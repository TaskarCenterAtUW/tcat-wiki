---
uid: 55f541aa-0bca-4b21-88f1-4dbd5c4f543a
title: How do quest definitions target element types?
slug: quest-definition-element-targeting
doc_type: concept
questions:
    - How do quest definitions target element types?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - editing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-27
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A quest definition targets a feature without a valid matching element query.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest-definition-application.md
tags:
    - Assistant
---

<!-- @format -->

# How do quest definitions target element types?

## Short Answer

A quest definition can target features by their element type and tags, then present questions for matching features.

## Significance

This connects a field form to the feature it is intended to describe.

## What This Means

Define the matching query and the questions for the selected element. The documented syntax supports tag presence or absence, exact and regular-expression values, numeric or date comparisons, and `and`/`or` expressions with parentheses. Multiple element types can be targeted together by separating them with a comma, for example `nodes, ways`. A feature-presets block can also define which new features a contributor may add. For example, a curb-ramp preset can use the OpenSidewalks tag `barrier=kerb` and target the resulting feature with an element query specified in the quest definition.

## What This Does Not Mean

A quest does not appear on unrelated features automatically, and defining a feature preset does not make every possible feature type available for addition.

## How To Use This

Test the query against the workspace data and review the resulting change set. If contributors should add new features from the app, define only the needed feature presets.

## Example

Examples include `ways`, `ways with (footway=sidewalk)`, `ways with (footway=sidewalk and !surface)`, `nodes with (barrier=kerb and !tactile_paving)`, and `ways, nodes with (footway=sidewalk or ext:new_sidewalk=yes)`.

## Assistant Guidance

Explain the element query concept and provide a link to the [Element Query Documentation](../../../aviv-scoutroute/quests/element-query.md).

## Related Concepts

- [How is a quest definition applied?](quest-definition-application.md)

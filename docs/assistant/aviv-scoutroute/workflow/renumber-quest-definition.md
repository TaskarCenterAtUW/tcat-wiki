---
uid: 2e7b60cf-9c49-4e25-974c-ab4ce9d2105b
title: How do I renumber an AVIV ScoutRoute quest definition?
slug: renumber-quest-definition
doc_type: workflow
questions:
    - How do I renumber an AVIV ScoutRoute quest definition?
    - How does the Quest Definition Creator update question IDs?
    - Do quest dependencies stay connected after renumbering?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The Quest Definition Creator automatically renumbers every unchanged quest in a definition.
        - Moving an element changes question IDs without updating their dependencies.
        - Automatic renumbering of a quest definition removes its dependencies.
related_pages:
    - ../concept/quest-definition-creator.md
    - ../concept/quest-definition-element-targeting.md
    - ../concept/quest-dependency-evaluators.md
    - upgrade-quest-definition.md
tags:
    - Assistant
---

<!-- @format -->

# How do I renumber an AVIV ScoutRoute quest definition?

## Short Answer

Use the Quest Definition Creator's element-order controls to renumber the questions associated with an element. When an element is reordered, the Creator remaps the affected question IDs and carries their answer dependencies to the new IDs.

## Significance

Reordering through the Creator can reduce manual ID editing and help preserve conditional quest logic in complex definitions.

## What This Means

1. Load the existing Quest Definition into the Creator.
2. Move the element up or down to its intended position. If needed, move it away and back to its original position to trigger the update.
3. Review the new question IDs in the definition.
4. Check that answer dependencies refer to the remapped question IDs.
5. Use the validation result and JSON preview to inspect the complete definition before exporting it.

The Creator updates the numbering associated with elements that are changed. Elements that are not changed may retain their existing numbering.

## What This Does Not Mean

Renumbering does not change the meaning of a question or automatically renumber every unchanged element's quests. It also does not remove dependencies; dependencies are updated but should be checked after the Creator remaps the relevant question IDs.

## How To Use This

Keep a copy of the original definition before reordering. Make one ordering change at a time, then inspect the affected IDs and dependency references in the preview and exported JSON. Test the resulting conditional flow in the intended workspace.

## Example

An element's questions use IDs in the `1000` range, and the element is moved in the Creator. The Creator assigns the element's questions IDs in the range associated with its new position, such as `200`, and updates a dependent question to refer to the new ID. Other elements that were not moved retain their existing numbering until their quests or their ordering are changed.

## Assistant Guidance

Explain that the remapping applies to affected elements, not necessarily to every question in the entire definition. Do not recommend editing IDs manually when avoidable.

## Related Concepts

- [What is the AVIV ScoutRoute Quest Definition Creator?](../concept/quest-definition-creator.md)
- [How do quest definitions target element types?](../concept/quest-definition-element-targeting.md)
- [What are AVIV ScoutRoute quest dependency evaluators?](../concept/quest-dependency-evaluators.md)
- [How do I upgrade an AVIV ScoutRoute quest definition?](upgrade-quest-definition.md)

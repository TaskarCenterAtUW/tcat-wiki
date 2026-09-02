---
uid: 3ef13a7d-44e9-4ebf-9c27-02a007db6795
title: What are AVIV ScoutRoute quest feature presets?
slug: quest-definition-feature-presets
doc_type: concept
questions:
    - What are AVIV ScoutRoute quest feature presets?
    - What can an AVIV ScoutRoute feature preset create?
    - Can a feature preset set multiple tags?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - editing
    - data-collection
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
        - A feature preset can create arbitrary line or area geometry from the mobile app.
        - A feature preset lets the mobile user customize its configured tags.
        - A feature preset automatically creates a complete survey workflow without a matching quest definition.
related_pages:
    - quest-definition-element-targeting.md
    - quest-definition-creator.md
    - ../../workspaces/concept/mobile-point-feature-creation.md
tags:
    - Assistant
---

<!-- @format -->

# What are AVIV ScoutRoute quest feature presets?

## Short Answer

A feature preset is a Quest Definition configuration that lets an AVIV ScoutRoute mobile user add a predefined point feature to the map. The preset supplies the feature name, icon, and one or more tags. A separate quest can target those tags and collect more information.

## Significance

Feature presets support field workflows for adding discrete features that are missing from the mapped data without requiring mobile users to construct geometry or choose tags manually.

## What This Means

A user long-presses a map location and selects an available feature preset. The app creates a point feature with the preset's configured tags. The user may also be able to attach a note or picture through the app's feature-creation flow.

A preset can set multiple tags on the created feature. For example, a lowered-curb preset could create a point with `barrier=kerb` and `kerb=lowered`. A quest definition can then target features that match those tags and present follow-up questions.

Feature presets currently apply to point or node geometry only. The available presets are defined by the Quest Definition author; they are not an unrestricted list of every possible feature type.

## What This Does Not Mean

A feature preset does not let the mobile user customize the preset's tags, and creating a point does imply the ability to create a line or area feature. A preset also does not replace the separate quest configuration needed to ask follow-up questions.

## How To Use This

Define only the point features that field users should be able to add. Give each preset a clear name and supported icon, configure all required tags, and test the resulting feature in the target workspace. If additional information is needed, create a quest whose element query matches the preset's tags.

## Example

A mapping project defines a **Lowered Curb** preset with the tags `barrier=kerb` and `kerb=lowered`. A contributor adds the preset at the curb's location. AVIV ScoutRoute creates the tagged point, and a separate curb quest can target that combination to ask about condition or measurements.

## Assistant Guidance

Ask which point feature the user wants to add, which tags should identify it, and whether follow-up questions are required. Do not promise support for line or area creation through feature presets. Treat exact app behavior as version-dependent and distinguish the Quest Definition schema and configuration from its implementation in the app.

## Related Concepts

- [How do quest definitions target element types?](quest-definition-element-targeting.md)
- [What is the AVIV ScoutRoute Quest Definition Creator?](quest-definition-creator.md)
- [What can AVIV ScoutRoute create on mobile?](../../workspaces/concept/mobile-point-feature-creation.md)

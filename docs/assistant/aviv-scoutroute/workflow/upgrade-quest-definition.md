---
uid: e666abac-7806-4f58-a9b8-48a70cc8bdb6
title: How do I upgrade an AVIV ScoutRoute quest definition?
slug: upgrade-quest-definition
doc_type: workflow
questions:
    - How do I upgrade an AVIV ScoutRoute quest definition?
    - How do I update an older Long Form Quest Definition?
    - Where can I find the latest schema version supported by the Quest Definition Creator?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - formats
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
        - The Quest Definition Creator can upgrade every older Long Form Quest Definition automatically.
        - Upgrading a Quest Definition automatically updates the workspace that uses it.
        - The schema version shown in one Creator release remains the latest supported version forever.
related_pages:
    - ../concept/quest-definition-creator.md
    - ../concept/quest-definition-application.md
    - update-quest-definition-in-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# How do I upgrade an AVIV ScoutRoute quest definition?

## Short Answer

Load the existing Long Form Quest Definition into the Quest Definition Creator and use its upgrade control when the loaded version is compatible with the supported schema version. The latest supported schema version is listed in the footer at the bottom of the page.

## Significance

Upgrading through the Creator can apply a supported schema-version change while preserving the definition's editable structure for review.

## What This Means

1. Open the Quest Definition Creator and load the existing definition file.
2. Check the definition's loaded schema version and the latest supported Long Form Quest Definition schema version shown in the footer.
3. If the Creator offers an upgrade, select it.
4. Review the updated definition in the live preview and validation panels.
5. Inspect the generated JSON and export the upgraded definition.
6. Update the intended workspace configuration and reload the configuration in AVIV ScoutRoute before testing.

The upgrade control is available only when the Creator supports the relevant compatibility path. If no upgrade is offered, do not assume that manually changing the version field is sufficient.

## What This Does Not Mean

An upgrade does not guarantee that every semantic or workflow change is correct for the project. It also does not deploy the definition to a workspace automatically. A schema version displayed in the footer describes the Creator's current supported version.

## How To Use This

Keep the original definition as a backup. Record the loaded version, the supported version shown in the footer, the validation result, and the workspace tested. Test conditional questions, dependencies, icons, and other project-specific behavior after updating the workspace configuration.

## Example

A project manager loads a definition written for an older compatible schema. The Creator displays the supported schema version in its footer and offers an upgrade in the definition validation section. After selecting it, the manager reviews the updated preview and JSON, exports the result, updates the workspace configuration, and tests the definition in AVIV ScoutRoute.

## Assistant Guidance

Ask for the loaded schema version and the supported version shown in the Creator footer before describing an upgrade path. Do not claim that an unavailable upgrade control can be replaced safely by only editing the version string. Remind users that workspace configuration and app testing are separate steps.

## Related Concepts

- [What is the AVIV ScoutRoute Quest Definition Creator?](../concept/quest-definition-creator.md)
- [How is a quest definition applied?](../concept/quest-definition-application.md)
- [How do I update a quest definition in a workspace?](update-quest-definition-in-workspace.md)

---
title: What accessibility assumptions are built into AccessMap?
slug: accessibility-assumptions
doc_type: concept
questions:
    - What accessibility assumptions are built into AccessMap?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - routing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AccessMap's assumptions represent every traveler's needs.
        - A route based on AccessMap assumptions is an accessibility certification.
related_pages:
    - assistant/accessmap/concept/accessibility-needs.md
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What accessibility assumptions are built into AccessMap?

## Short Answer

AccessMap assumes that mapped pedestrian-network features and accessibility attributes can be used to compare routes under selected profiles and preferences. These assumptions are simplified, data-dependent, and version-sensitive.

## Significance

Making assumptions visible helps users interpret route results and identify when field knowledge or a different profile is needed.

## What This Means

- Check the selected profile, preferences, and dataset version.
- Consider missing, outdated, or uncertain attributes.
- Compare modeled results with local conditions for important trips.

## What This Does Not Mean

The assumptions do not describe every disability or guarantee that a route is usable, safe, or compliant with a legal standard. A map result is not a physical inspection.

## How To Use This

State the assumptions that affect the answer and cite the current AccessMap documentation. Avoid filling undocumented model behavior from general expectations.

## Example

A planner compares routes under two profiles and explains that the difference reflects profile and data assumptions rather than a universal accessibility ranking.

## Assistant Guidance

Do not present assumptions as facts about a person's ability or a site's compliance. Ask for the profile, location, and version, and abstain when critical assumptions are unknown.

## Related Concepts

- [Accessibility needs](accessibility-needs.md)
- [Mobility profiles](mobility-profiles.md)
- [Routing limitations](routing-limitations.md)

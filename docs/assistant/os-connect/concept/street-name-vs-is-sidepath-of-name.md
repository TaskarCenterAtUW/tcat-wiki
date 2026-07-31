---
title: What is the difference between street:name=* and is_sidepath:of:name=*?
slug: street-name-vs-is-sidepath-of-name
doc_type: concept
questions:
    - What is the difference between street:name=* and is_sidepath:of:name=*?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - osm-interoperability
    - editing
risk_level: medium
authority_level: explanatory
publication_status: draft
    last_reviewed: 2026-07-31
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Either tag proves accessibility, ownership, or connectivity.
    related_pages:
        - assistant/os-connect/concept/sidewalk-street-name-association.md
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between street:name=_ and is_sidepath:of:name=_?

## Short Answer

When working with OpenStreetMap (OSM) data, the name of the street parallel to a sidewalk may be represented as with either `street:name=StreetName` or `is_sidepath:of:name=StreetName`. These tags have the same meaning, and both tagging schemes are in use.

## Significance

Recognizing both forms supports consistent interpretation of OSM data.

## What This Means

Treat either tag as the name of the street associated with the adjacent sidewalk.

## What This Does Not Mean

Neither tag proves accessibility, ownership, or connectivity.

## How To Use This

When reading or transforming OSM data, recognize both tags. When editing, follow the tagging convention used by the relevant project or dataset.

## Example

A sidewalk beside Cedar Avenue may use either `street:name=Cedar Avenue` or `is_sidepath:of:name=Cedar Avenue`.

## Assistant Guidance

Explain that the two tags are equivalent in meaning and that both are in use. If the user asks about which one should be used, note that TCAT recommends `street:name`, while cautioning that `is_sidepath:of:name` is not wrong and that it is usually recommended to follow local best practices.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)

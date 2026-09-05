---
uid: a18f0418-5032-46cb-a66e-8576e1f3ab5b
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
last_reviewed: 2026-09-04
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

When working with OpenStreetMap (OSM) data, a separately mapped sidewalk may be associated with a parallel street using `street:name=StreetName` or `is_sidepath:of:name=StreetName`. Both patterns are in use, but do not assume they have identical support in every project or consumer. Check the current tagging guidance for the intended dataset and use `street:name` where the current project guidance recommends it.

## Significance

Recognizing both forms helps editors and data consumers interpret older or locally varied OSM tagging without confusing a street-name relationship with a physical network connection.

## What This Means

Treat either tag as a possible association between the adjacent sidewalk and street, then verify the intended convention and consumer support. Keep a separately mapped sidewalk as its own pedestrian geometry.

## What This Does Not Mean

Neither tag proves accessibility, ownership, or connectivity. The two patterns should not be described as universally interchangeable without checking the relevant project and consumer.

## How To Use This

When reading or transforming OSM data, recognize both tags and preserve the source convention where appropriate. When editing, follow the current convention used by the relevant project, schema, and downstream consumer; current TCAT guidance increasingly uses `street:name` for this association.

## Example

A sidewalk beside Cedar Avenue may contain `street:name=Cedar Avenue` in a project that follows current TCAT guidance, while an older or locally maintained dataset may contain `is_sidepath:of:name=Cedar Avenue`. An importer should recognize both and document any normalization.

## Assistant Guidance

Explain that both tags are used to associate a sidewalk with a street, but avoid claiming universal equivalence across consumers. If the user asks which one to use, cite the current project guidance, note TCAT's current preference for `street:name`, and advise checking local or downstream requirements before changing existing data.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)

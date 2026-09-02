---
uid: e31794c6-04da-4a09-8e70-d1548a535722
title: What input does a Walksheds batch amenity request need?
slug: walkshed-batch-amenity-input
doc_type: concept
questions:
    - What input does a Walksheds batch amenity request need?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - destinations
    - formats
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A batch request needs every attribute from a POI export.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What input does a Walksheds batch amenity request need?

## Short Answer

Batch walksheds primarily need the coordinates of the origin or amenity locations, in the current required CSV format.

## Significance

A simple coordinate input can support many repeated analyses, but the current interface may require clearer preparation guidance.

## What This Means

Export or prepare the required coordinates and headers before uploading.

## What This Does Not Mean

Names and source metadata may not be consumed by the batch calculation even when they are useful to the project.

## How To Use This

Keep names and source records separately so results can be matched back to locations.

## Example

A park export is reduced to labeled coordinates for a batch request.

## Assistant Guidance

Verify the current input schema and preserve the original POI dataset.

## Related Concepts

- [What input does Walksheds batch processing use?](walkshed-batch-input.md)

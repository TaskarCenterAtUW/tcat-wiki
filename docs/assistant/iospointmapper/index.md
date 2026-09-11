---
uid: d78da859-7f3a-4dc2-9a85-f1e6e64d66e5
title: iOSPointMapper — Assistant Knowledge Base
slug: iospointmapper-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the iOSPointMapper knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - iOSPointMapper
topics:
    - iospointmapper
    - tdei-ecosystem
    - data-collection
    - field-data-collection
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - iOSPointMapper supports every Apple device or iOS version.
        - iOSPointMapper automatically publishes collected observations.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
tags:
    - Assistant
---

<!-- @format -->

# iOSPointMapper — Assistant Knowledge Base

## Short Answer

This section is reserved for verified assistant guidance about iOSPointMapper, including supported devices, field data collection, and how collected observations move through the TCAT data workflow. Product-specific answers require current iOSPointMapper documentation.

## Significance

Accurate device and collection guidance prevents users from beginning a field survey with unsupported hardware or misunderstanding what happens to captured data.

## What This Means

 - Use the device-compatibility article for supported hardware and operating-system information.
 - Use the collection workflow for the current setup and survey sequence.
 - Confirm current release documentation before giving version-specific advice.

## What This Does Not Mean

The presence of this knowledge-base section does not establish support for a particular device, operating-system release, sensor, or upload destination.

## How To Use This

Users should provide the device model, operating-system version, and intended collection task when requesting help. Maintainers should update this section only from authoritative product evidence.

## Example

A user asks whether a particular iPhone can collect a point survey. The assistant asks for the model and iOS version, then answers only from the current compatibility evidence.

## Assistant Guidance

This section has limited verified source material. Cite the relevant product documentation and abstain when device support, collection behavior, or data handling is not documented.

## Related Concepts

 - [What devices are compatible with iOSPointMapper?](concept/device-compatibility.md)
 - [How do I start collecting data using iOSPointMapper?](workflow/start-collecting-data.md)

---
uid: 9e865fd0-fe83-4ee2-be27-e8d0a179b590
title: How does AVIV ScoutRoute handle downloaded data and uploads?
slug: offline-data-and-upload
doc_type: concept
questions:
    - How does AVIV ScoutRoute handle downloaded data and uploads?
    - Can I download AVIV ScoutRoute data before a field survey?
audiences:
    - advocate
    - public
    - planner
    - developer
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - data-freshness
    - field-data-collection
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Downloading map data guarantees that all field submissions can be completed without connectivity.
        - Downloaded data is necessarily current after it is stored on the device.
related_pages:
    - ../workflow/manage-quest-visibility.md
    - quest-contributions.md
    - ../../../aviv-scoutroute/user-manual/app-settings.md
tags:
    - Assistant
---

<!-- @format -->

# How does AVIV ScoutRoute handle downloaded data and uploads?

## Short Answer

AVIV ScoutRoute can download data for the visible map area and can be configured to upload completed answers automatically or keep them locally until manual upload, according to the current app settings documentation.

## Significance

Preloading data can help contributors prepare for areas with poor cellular connectivity, while upload settings affect when contributions leave the device.

## What This Means

Move the map to the survey area, select **Download data here**, and allow the visible-area data to download. In Communication settings, **Upload answers automatically** controls whether completed answers sync immediately or remain local until manual upload.

## What This Does Not Mean

Downloaded data is not a guarantee of current information or complete offline functionality. Upload timing and behavior can depend on app version, platform, connectivity, and project configuration.

## How To Use This

Download the relevant area before a survey when appropriate, confirm the upload setting, and verify that contributions have synchronized according to project procedures.

## Example

A contributor uses Wi-Fi to download the visible survey area before walking a route, then checks the upload setting before submitting observations.

## Assistant Guidance

Ask for platform, app version, connectivity, download area, and upload setting. Do not promise that a downloaded area supports every offline operation.

## Related Concepts

- [What do quest contributions change?](quest-contributions.md)
- [What is a quest?](quest.md)

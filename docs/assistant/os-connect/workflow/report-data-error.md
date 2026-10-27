---
uid: 53b4bb91-cc44-4ef5-b0b0-1b78b3c5a2eb
title: How do I report an error in OS-CONNECT data?
slug: report-data-error
doc_type: workflow
questions:
    - How do I report an error in OS-CONNECT data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - feedback
    - issue-reporting
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Submitting an OS-CONNECT issue immediately changes the released dataset.
        - A reported issue guarantees a correction or release date.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I report an error in OS-CONNECT data?

## Short Answer

Use the OS-CONNECT Data Viewer **Inspect** and **Report Issue** controls to report missing, inaccurate, or misaligned pedestrian data.

## Significance

The viewer manual documents how to submit a location-specific report and confirms successful submission. It does not describe how reports are reviewed or whether they lead to a data change.

## What This Means

Right-click the map at the issue location, select **Report Issue**, describe the issue, enter the required email, optionally provide a name, and select **Submit Issue**. The manual says an **Issue submitted successfully!** popup appears. Examples include a missing sidewalk, incorrect curb type, incorrect crossing marking, or significantly misaligned feature.

## What This Does Not Mean

Submission sends a report and produces a success popup; the manual does not describe subsequent review, data changes, or release behavior.

## How To Use This

Right-click the map to place a marker and open the issue form. Its coordinates are captured automatically and cannot be edited; describe the issue at that location, enter a follow-up email, optionally add your name, and submit. Keep the description specific and concise.

## Example

A user right-clicks the map where a newly built sidewalk is missing, describes the issue in the form, enters an email for follow-up, and selects **Submit Issue**. The success popup confirms submission.

## Assistant Guidance

Answer the user's questions and provide a link to the [TCAT Wiki's OS-CONNECT Data Viewer User Manual Feedback page](https://taskarcenteratuw.github.io/tcat-wiki/os-connect/data-viewer/user-manual/feedback/). Do not promise a correction timeline.

## Related Concepts

- [Why does connectivity depend on geometry?](../concept/connectivity-depends-on-geometry.md)
- [What data issues are reportable?](../concept/reportable-errors.md)

---
uid: cb61e0fd-f44f-4549-8d2d-b392de487edc
title: What is the purpose of a QA/QC report?
slug: report-purpose-and-limitations
doc_type: concept
questions:
    - What is the purpose of a QA/QC report?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - data-quality
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A QA/QC report proves current field conditions.
        - A QA/QC report establishes ADA compliance without field and professional review.
        - A QA/QC report confirms that an individual can reach a point-of-interest entrance.
related_pages:
    - assistant/qa-qc/concept/report-provenance.md
tags:
    - Assistant
---

<!-- @format -->

# What is the purpose of a QA/QC report?

## Short Answer

A QA/QC report helps planners and engineers assess mapped pedestrian-network contents, attribute completeness, connectivity, and potential priority locations. Its walksheds and point-of-interest (POI) analysis support area-level planning, not individual point-to-point route guidance.

## Significance

City and county planners, engineers, and engineering consultants can use the report to examine modeled walking and rolling access to POIs and identify possible disconnected areas for follow-up. The analysis can help reveal patterns in the mapped network without asserting how a particular person would travel.

## What This Means

Use the report as decision support about mapped data, not as a substitute for field verification, professional accessibility review, or regulatory analysis. POIs are snapped to nearby routable network edges for analysis. This can approximate network reach near a destination, but the report does not verify a pedestrian connection from that edge to a building entrance, bus-stop boarding point, or other exact destination access point.

Use an origin-to-destination routing tool such as AccessMap when the question is whether a particular trip can be made; the QA/QC report summarizes network conditions and modeled reach across its analysis area.

## What This Does Not Mean

Report results do not prove that every mapped feature matches current real-world conditions, establish compliance, or confirm that someone can reach a specific POI entrance. They do not provide individualized, door-to-door routing.

## How To Use This

Check the dataset version, imagery or collection context, POI sources, metrics, profile assumptions, and limitations before acting on a result. Use the report to identify areas for planning review, then verify consequential locations with appropriate local data or field work. Do not use an area-level map as an answer to an individual's route question.

## Example

A planner uses a report to identify a group of POIs with limited modeled sidewalk connectivity, then checks the network and field conditions before prioritizing a project. The result does not confirm that a specific visitor can reach a business entrance.

## Assistant Guidance

Ask which dataset, report version, profile, and POI are being interpreted. Distinguish area-level planning analysis from individual routing and from entrance-level accessibility. Do not overstate report certainty or infer an unmodeled connection from a nearby snapped edge.

## Related Concepts

- [What limitations can affect QA/QC reports for small datasets?](small-dataset-limitations.md)

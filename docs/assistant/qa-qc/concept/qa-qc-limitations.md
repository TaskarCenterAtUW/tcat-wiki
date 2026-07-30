---
title: What Are the Limitations of QA/QC Analysis?
slug: qa-qc-limitations
doc_type: concept
questions:
    - What Are the Limitations of QA/QC Analysis?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
    - Walksheds
topics:
    - qa-qc
    - completeness
    - data-freshness
    - accessibility-data
    - os-connect
    - walksheds
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - QA/QC analysis is based on current or real-time data.
        - The completeness report certifies ADA compliance or legal conformance.
        - Walkshed metrics in the QA/QC report cover all possible origin points, not just POIs.
        - The QA/QC report reflects the current real-world state of pedestrian infrastructure.
related_pages:
    - assistant/qa-qc/index.md
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/qa-qc-report.md
    - assistant/cross-platform/concept/completeness.md
    - assistant/cross-platform/concept/ada-compliance-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# What Are the Limitations of QA/QC Analysis?

## Short Answer

The QA/QC analysis for OS-CONNECT has several important limitations. Imagery vintage and dataset release vary by report, so users must check report provenance before interpreting the analysis as current. The completeness metrics measure how well pedestrian network elements are tagged against OS-CONNECT schema requirements — not whether those elements meet ADA accessibility standards. Walkshed metrics may be calculated only from points of interest (POIs), not from all possible origin locations, so users should verify the report's methodology before treating them as a comprehensive accessibility map.

## Significance

Understanding the limitations of QA/QC analysis is critical for planners, jurisdictions, and advocates who rely on OS-CONNECT data to make decisions. Mistaking a completeness score for ADA compliance could lead agencies to misallocate resources or incorrectly claim regulatory conformance. Recognizing that the underlying imagery is from 2023 — not current — prevents jurisdictions from assuming the data captures recent construction, sidewalk repairs, or curb ramp installations. For advocates, knowing that Walkshed metrics are POI-based helps avoid overstating reachability to destinations that may not be included in the analysis.

## What This Means

- The QA/QC report reflects a snapshot tied to its documented imagery, dataset release, and processing date — it is not a live or continuously updated assessment.
- Completeness scores measure schema conformance (are the OS-CONNECT attributes populated?), not the physical accessibility of sidewalks, crossings, or curb ramps in the real world.
- Walkshed metrics in the QA/QC report are calculated from POIs only, so areas not near an included POI may appear to have less reachability than they actually have for residents walking to other destinations.
- Changes to on-the-ground infrastructure — new sidewalks, curb ramps, or construction detours — that occurred after the report's source imagery or dataset release are not always reflected in the analysis.

## What This Does Not Mean

- It does not mean the QA/QC report can be used to certify ADA compliance or demonstrate regulatory conformance.
- It does not mean that a high completeness score indicates a barrier-free pedestrian environment — gaps in the real world may still exist even when tags are complete.
- It does not mean Walkshed-based metrics cover all possible walking destinations; they are limited to the POIs included in the analysis.
- It does not mean the data reflects current conditions; infrastructure may have changed since the report's source imagery was captured or dataset was released.

## How To Use This

**Planners**: Use QA/QC completeness scores to identify areas where OS-CONNECT data may be under-tagged and in need of enrichment, but do not substitute them for field-verified ADA compliance assessments. Cross-reference the report's findings with local knowledge of recent infrastructure changes.

**Jurisdictions**: Check the report's documented imagery and dataset vintage; more recent sidewalk projects, curb ramp installations, or street redesigns may not appear in the QA/QC analysis. Use the report as a baseline for stewardship prioritization, not as a current-state inventory.

**Advocates**: Use Walkshed metrics to highlight connectivity gaps to key POIs, but understand that the analysis may not include all destinations relevant to your community. Supplement with direct community knowledge when making the case for infrastructure investment.

**Public**: The QA/QC report helps explain what the OS-CONNECT dataset contains and where data is thin, but it does not necessarily describe the current walking experience on the ground. Check the underlying imagery date before drawing conclusions.

## Example

A city planner in Spokane reviews the QA/QC report for their jurisdiction and sees a completeness score of 92%. They are preparing an ADA transition plan and consider citing this score as evidence of sidewalk network completeness. After understanding the limitations, they recognize that the 92% reflects only how well the features are tagged against the OS-CONNECT schema, not whether those sidewalks meet ADA slope, width, or surface requirements. They also note that a major downtown sidewalk reconstruction completed in 2025 is absent from the 2023-imagery-based data. The planner instead uses the QA/QC report to prioritize field-validation work and identifies areas where schema tagging is incomplete, while commissioning a separate ADA compliance audit.

## Assistant Guidance

Cite this page whenever a user asks whether QA/QC results constitute current or compliance-grade data. Abstain from answering if the user's jurisdiction, desired imagery vintage, or specific dataset release is unknown — these contexts materially affect the applicability of the analysis. Do not claim that the QA/QC report reflects current real-world conditions, that it certifies ADA compliance, or that Walkshed metrics cover all possible origins. Recommend that users consult their jurisdiction's own infrastructure records and field surveys for ADA compliance determinations.

## Related Concepts

- [OS-CONNECT knowledge base](../../os-connect/index.md)
- [What is a QA/QC report?](../../os-connect/concept/qa-qc-report.md)
- [What does completeness mean?](completeness.md)
- [Is completeness the same as ADA compliance?](../../cross-platform/concept/ada-compliance-boundaries.md)

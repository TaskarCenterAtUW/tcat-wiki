---
title: Support intents (RAG routing)
tags:
    - Assistant
slug: support-intents
doc_type: workflow
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
audiences:
    - planner
    - jurisdiction
topics:
    - support
    - intent
    - helpline
risk_level: low
authority_level: draft
review_status: draft
last_reviewed: 2026-05-18
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/support/workflow/support-answer-patterns.md
---

<!-- @format -->

# Support intents (RAG routing)

## Short Answer

This section catalogs named retrieval intents — patterns of user queries that map to specific knowledge-base pages. Intents help retrieval pipelines route ambiguous questions to the most relevant pages without requiring exact keyword matches.

## Significance

Support staff ask operational questions in the moment and may phrase similar questions in many different ways. Intents bundle the right question pages (ecosystem, downloads, corrections, GTFS Pathways, OSM tagging, Mappy Hours) for grounded replies.

## Intent catalog

### `explain-ecosystem`

**Example query:** A partner is confused about TDEI, OS-CONNECT, OpenSidewalks, and OSM. Give a short explanation of how they relate.

**Retrieve these pages:**

- [tdei-os-connect-osm-differences](support/concept/tdei-os-connect-osm-differences.md)
- [tdei](tdei/concept/tdei.md)
- [os-connect](os-connect/concept/os-connect.md)
- [opensidewalks](os-connect/concept/opensidewalks.md)

### `recommend-dataset`

**Example query:** An agency wants pedestrian walkway data for bus stop planning in ArcGIS. Which dataset and format should we recommend?

**Retrieve these pages:**

- [choose-dataset-for-arcgis](support/workflow/choose-dataset-for-arcgis.md)
- [choose-dataset-for-planning](support/workflow/choose-dataset-for-planning.md)

### `guide-download`

**Example query:** A user downloaded the wrong file from TDEI. How should we help them find the correct released OS-CONNECT dataset?

**Retrieve these pages:**

- [mislabeled-dataset-handling](tdei/concept/mislabeled-dataset-handling.md)
- [download-os-connect-data](tdei/workflow/download-os-connect-data.md)
- [released-dataset](tdei/concept/released-dataset.md)

### `explain-osw-format`

**Example query:** What does an OSW download contain, and how do edges and nodes map to sidewalks, crossings, and curb ramps?

**Retrieve these pages:**

- [osw-download-contents](tdei/concept/osw-download-contents.md)
- [osw-edges-and-nodes](tdei/concept/osw-edges-and-nodes.md)

### `support-arcgis-use`

**Example query:** How should I explain importing OS-CONNECT GeoJSON into ArcGIS?

**Retrieve these pages:**

- [import-into-arcgis](os-connect/workflow/import-into-arcgis.md)
- [gis-software-compatibility](os-connect/concept/gis-software-compatibility.md)

### `handle-mislabeled-datasets`

**Example query:** A public dataset appears mislabeled or points to a wrong download. What should support staff say and do?

**Retrieve these pages:**

- [mislabeled-dataset-handling](tdei/concept/mislabeled-dataset-handling.md)

### `explain-issue-reporting`

**Example query:** A user found a railroad track incorrectly marked as a walkway. How should they report it?

**Retrieve these pages:**

- [report-data-error](os-connect/workflow/report-data-error.md)
- [reportable-errors](os-connect/concept/reportable-errors.md)

### `explain-correction-lifecycle`

**Example query:** How long does it take for submitted corrections to appear in OS-CONNECT?

**Retrieve these pages:**

- [correction-release-lag](os-connect/concept/correction-release-lag.md)
- [issue-report-follow-up](os-connect/concept/issue-report-follow-up.md)

### `distinguish-release-from-review`

**Example query:** Does submitting an issue immediately change the public dataset?

**Retrieve these pages:**

- [issue-report-auto-update](os-connect/concept/issue-report-auto-update.md)

### `handle-bulk-corrections`

**Example query:** An agency has many known sidewalk errors. Should they submit them individually or coordinate a structured review?

**Retrieve these pages:**

- [bulk-correction-submission](os-connect/concept/bulk-correction-submission.md)

### `validate-authority`

**Example query:** A partner asks whether this is the authoritative pedestrian dataset for their jurisdiction. What can we safely say?

**Retrieve these pages:**

- [dataset-authority](support/concept/dataset-authority.md)

### `explain-gtfs-pathways-relationship`

**Example query:** A transit agency asks whether OS-CONNECT is a substitute for GTFS Pathways.

**Retrieve these pages:**

- [os-connect-vs-gtfs-pathways](support/concept/os-connect-vs-gtfs-pathways.md)

### `check-gtfs-pathways-availability`

**Example query:** How can someone tell whether a GTFS feed includes pathways.txt?

**Retrieve these pages:**

- [check-gtfs-feed-pathways](support/workflow/check-gtfs-feed-pathways.md)

### `support-trip-planning-vendors`

**Example query:** A trip planner has poor walking directions because sidewalks lack street-name references. What should we explain?

**Retrieve these pages:**

- [missing-street-names-for-vendors](os-connect/concept/missing-street-names-for-vendors.md)

### `explain-osm-sidewalk-naming-tags`

**Example query:** What are street:name and is_sidepath:of:name, and when should they be used?

**Retrieve these pages:**

- [street-name-vs-sidepath-name](os-connect/concept/street-name-vs-sidepath-name.md)

### `recommend-osm-tagging-practice`

**Example query:** Which tag should we recommend for associating sidewalks with street names?

**Retrieve these pages:**

- [recommended-sidewalk-tagging-pattern](os-connect/concept/recommended-sidewalk-tagging-pattern.md)

### `connect-mapping-to-routing`

**Example query:** Why does sidewalk tagging matter for navigation instructions?

**Retrieve these pages:**

- [street-name-routing-importance](os-connect/concept/street-name-routing-importance.md)

### `explain-walksheds`

**Example query:** How should support staff explain Walksheds to a transit planner?

**Retrieve these pages:**

- [walkshed](walksheds/concept/walkshed.md)
- [os-connect-data-usage](walksheds/concept/os-connect-data-usage.md)

### `explain-accessmap`

**Example query:** How is AccessMap different from Walksheds?

**Retrieve these pages:**

- [accessmap-vs-walksheds](support/concept/accessmap-vs-walksheds.md)

### `support-stop-planning`

**Example query:** How can OS-CONNECT and Walksheds help with bus stop placement or access analysis?

**Retrieve these pages:**

- [os-connect-walksheds-bus-stop-planning](support/concept/os-connect-walksheds-bus-stop-planning.md)

### `support-event-accessibility`

**Example query:** How can OS-CONNECT support FIFA or major-event accessibility planning?

**Retrieve these pages:**

- [major-event-accessibility-planning](os-connect/concept/major-event-accessibility-planning.md)

### `support-school-access`

**Example query:** How can pedestrian accessibility data be used around schools and transit stops?

**Retrieve these pages:**

- [destination-access-analysis](os-connect/concept/destination-access-analysis.md)

### `explain-community-mapping-pathways`

**Example query:** A local mapping group wants to restart sidewalk mapping. What support can TCAT offer?

**Retrieve these pages:**

- [tcat-mapping-project-support](os-connect/concept/tcat-mapping-project-support.md)

### `explain-tasking-manager-status`

**Example query:** What happened to the old MapWith.ai Tasking Manager, and what should we recommend now?

**Retrieve these pages:**

- [mapwithai-workflow-history](os-connect/concept/mapwithai-workflow-history.md)

### `onboard-new-mappers`

**Example query:** What beginner materials should we share with sidewalk mappers?

**Retrieve these pages:**

- [mapper-training-materials](os-connect/concept/mapper-training-materials.md)

### `decide-mapping-priorities`

**Example query:** How should a community decide where to start mapping sidewalks?

**Retrieve these pages:**

- [mapping-prioritization](os-connect/concept/mapping-prioritization.md)

### `explain-data-quality-expectations`

**Example query:** When can volunteer-contributed sidewalk data become useful for agency planning?

**Retrieve these pages:**

- [community-data-usability](os-connect/concept/community-data-usability.md)

### `refer-to-mappy-hours`

**Example query:** When is Mappy Hours the right next step?

**Retrieve these pages:**

- [mappy-hours-referral-decision](support/workflow/mappy-hours-referral-decision.md)

### `decide-direct-support-vs-office-hours`

**Example query:** When should staff answer directly instead of referring someone to Mappy Hours?

**Retrieve these pages:**

- [mappy-hours-referral-decision](support/workflow/mappy-hours-referral-decision.md)

### `draft-professional-support-response`

**Example query:** Draft a professional response to an agency partner asking about OS-CONNECT correction timelines.

**Suggested pattern:** `answer-known-operational`

**Retrieve these pages:**

- [correction-release-lag](os-connect/concept/correction-release-lag.md)

### `soften-support-tone`

**Example query:** Rewrite this support email to be warmer but less casual and more technically precise.

**Suggested pattern:** `answer-when-uncertain`

**Retrieve these pages:**

### `manage-uncertainty`

**Example query:** Rewrite this answer so it does not overstate what we know.

**Suggested pattern:** `answer-when-uncertain`

**Retrieve these pages:**

### `preserve-relationship-continuity`

**Example query:** Draft a reply to a partner who is reconnecting after several months about a paused sidewalk-mapping project.

**Suggested pattern:** `reconnect-prior-collaborator`

**Retrieve these pages:**

### `identify-ownership`

**Example query:** This question crosses data, portal, and mapping workflows. Who should own the follow-up?

**Retrieve these pages:**

- [cross-team-followup-ownership](support/concept/cross-team-followup-ownership.md)

### `propose-next-step`

**Example query:** A partner has a practical use case but we do not yet know the answer. What should we say next?

**Suggested pattern:** `answer-when-uncertain`

**Retrieve these pages:**

- [handle-unknown-questions](support/workflow/handle-unknown-questions.md)

## What This Means

- `intents.md` maps common helpline and Question Board queries to their canonical knowledge base pages.

## What This Does Not Mean

- Not an exhaustive list of every user utterance.
- Not automated routing without human review for high-risk topics.
- Not a substitute for the [dispatch](dispatch.md) as the authoritative file registry.
- Not product documentation; intents are operational metadata for retrieval systems.

## How To Use This

**Assistants**: Index this page and linked question pages together. At query time, classify to an intent ID, fetch related pages, then apply a support answer pattern when drafting.

**Integrators**: Load intent mappings from `intents/support-intents.md` into your retrieval pipeline's query routing layer. When a user query matches an intent pattern, retrieve the mapped page directly.

**Authors**: Add intent entries to `support-intents.md` when helpline experience reveals new query patterns not captured by existing page titles.

## Assistant Guidance

Intents are metadata for retrieval pipelines, not content for end users. Do not surface intent categories directly in responses; use them only for internal routing.

## Related Concepts

- [Dispatch](dispatch.md)

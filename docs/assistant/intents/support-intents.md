---
title: Support intents (RAG routing)
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
  - assistant/workflows/support-answer-patterns.md
  - assistant/backlog/helpline-faq-backlog.md
---

# Support intents (RAG routing)

## Short Answer

Answerable **intents** map real helpline questions to factual pages and optional [answer patterns](../workflows/support-answer-patterns.md). Use them to route RAG retrieval and staff copilots toward multi-page answers instead of single random chunks.

## Significance

Support staff ask operational questions in the moment. Intents bundle the right question pages (ecosystem, downloads, corrections, GTFS Pathways, OSM tagging, Mappy Hours) for grounded replies.

## Intent catalog

### `explain-ecosystem`

**Example query:** A partner is confused about TDEI, OS-CONNECT, OpenSidewalks, and OSM. Give a short explanation of how they relate.

**Retrieve these pages:**

- [what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap](../questions/support/what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap.md)
- [what-is-tdei](../questions/tdei/what-is-tdei.md)
- [what-is-os-connect](../questions/os-connect/what-is-os-connect.md)
- [what-is-opensidewalks](../questions/os-connect/what-is-opensidewalks.md)

### `recommend-dataset`

**Example query:** An agency wants pedestrian walkway data for bus stop planning in ArcGIS. Which dataset and format should we recommend?

**Retrieve these pages:**

- [which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis](../questions/support/which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis.md)
- [which-dataset-should-i-use-if-i-need-pedestrian-walkway-data-for-planning](../questions/support/which-dataset-should-i-use-if-i-need-pedestrian-walkway-data-for-planning.md)

### `guide-download`

**Example query:** A user downloaded the wrong file from TDEI. How should we help them find the correct released OS-CONNECT dataset?

**Retrieve these pages:**

- [what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file](../questions/tdei/what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file.md)
- [where-do-i-download-os-connect-data](../questions/tdei/where-do-i-download-os-connect-data.md)
- [what-does-released-dataset-mean-in-tdei](../questions/tdei/what-does-released-dataset-mean-in-tdei.md)

### `explain-osw-format`

**Example query:** What does an OSW download contain, and how do edges and nodes map to sidewalks, crossings, and curb ramps?

**Retrieve these pages:**

- [what-files-are-included-in-an-osw-download](../questions/tdei/what-files-are-included-in-an-osw-download.md)
- [what-are-edges-and-nodes-in-the-osw-download](../questions/tdei/what-are-edges-and-nodes-in-the-osw-download.md)

### `support-arcgis-use`

**Example query:** How should I explain importing OS-CONNECT GeoJSON into ArcGIS?

**Retrieve these pages:**

- [how-do-i-import-os-connect-osw-geojson-into-arcgis](../questions/os-connect/how-do-i-import-os-connect-osw-geojson-into-arcgis.md)
- [can-os-connect-data-be-used-in-arcgis](../questions/os-connect/can-i-use-this-in-arcgis-or-qgis.md)

### `handle-mislabeled-datasets`

**Example query:** A public dataset appears mislabeled or points to a wrong download. What should support staff say and do?

**Retrieve these pages:**

- [what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file](../questions/tdei/what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file.md)

### `explain-issue-reporting`

**Example query:** A user found a railroad track incorrectly marked as a walkway. How should they report it?

**Retrieve these pages:**

- [how-do-i-report-an-error-in-os-connect-data](../questions/os-connect/how-do-i-report-an-error-in-os-connect-data.md)
- [what-kinds-of-errors-should-be-reported-through-the-os-connect-viewer](../questions/os-connect/what-kinds-of-errors-should-be-reported-through-the-os-connect-viewer.md)

### `explain-correction-lifecycle`

**Example query:** How long does it take for submitted corrections to appear in OS-CONNECT?

**Retrieve these pages:**

- [how-long-do-corrections-take-to-appear-in-a-public-release](../questions/os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md)
- [what-happens-after-i-submit-an-issue-report](../questions/os-connect/what-happens-after-i-submit-an-issue-report.md)

### `distinguish-release-from-review`

**Example query:** Does submitting an issue immediately change the public dataset?

**Retrieve these pages:**

- [do-reported-issues-automatically-update-the-public-dataset](../questions/os-connect/do-reported-issues-automatically-update-the-public-dataset.md)

### `handle-bulk-corrections`

**Example query:** An agency has many known sidewalk errors. Should they submit them individually or coordinate a structured review?

**Retrieve these pages:**

- [can-agencies-submit-bulk-corrections-or-priority-areas-for-review](../questions/os-connect/can-agencies-submit-bulk-corrections-or-priority-areas-for-review.md)

### `validate-authority`

**Example query:** A partner asks whether this is the authoritative pedestrian dataset for their jurisdiction. What can we safely say?

**Retrieve these pages:**

- [how-do-i-know-whether-a-dataset-is-authoritative](../questions/support/how-do-i-know-whether-a-dataset-is-authoritative.md)

### `explain-gtfs-pathways-relationship`

**Example query:** A transit agency asks whether OS-CONNECT is a substitute for GTFS Pathways.

**Retrieve these pages:**

- [how-is-os-connect-different-from-gtfs-pathways](../questions/support/how-is-os-connect-different-from-gtfs-pathways.md)

### `check-gtfs-pathways-availability`

**Example query:** How can someone tell whether a GTFS feed includes pathways.txt?

**Retrieve these pages:**

- [how-can-i-tell-whether-a-gtfs-feed-includes-pathways-txt](../questions/support/how-can-i-tell-whether-a-gtfs-feed-includes-pathways-txt.md)

### `support-trip-planning-vendors`

**Example query:** A trip planner has poor walking directions because sidewalks lack street-name references. What should we explain?

**Retrieve these pages:**

- [what-should-trip-planning-vendors-do-when-osm-pedestrian-paths-do-not-include-street-names](../questions/os-connect/what-should-trip-planning-vendors-do-when-osm-pedestrian-paths-do-not-include-street-names.md)

### `explain-osm-sidewalk-naming-tags`

**Example query:** What are street:name and is_sidepath:of:name, and when should they be used?

**Retrieve these pages:**

- [what-is-the-difference-between-street-name-and-is-sidepath-of-name](../questions/os-connect/what-is-the-difference-between-street-name-and-is-sidepath-of-name.md)

### `recommend-osm-tagging-practice`

**Example query:** Which tag should we recommend for associating sidewalks with street names?

**Retrieve these pages:**

- [which-sidewalk-to-street-name-tagging-pattern-is-currently-recommended](../questions/os-connect/which-sidewalk-to-street-name-tagging-pattern-is-currently-recommended.md)

### `connect-mapping-to-routing`

**Example query:** Why does sidewalk tagging matter for navigation instructions?

**Retrieve these pages:**

- [why-do-street-names-matter-for-walking-directions](../questions/os-connect/why-do-street-names-matter-for-walking-directions.md)

### `explain-walksheds`

**Example query:** How should support staff explain Walksheds to a transit planner?

**Retrieve these pages:**

- [what-is-a-walkshed](../questions/walksheds/what-is-a-walkshed.md)
- [how-does-walksheds-use-os-connect-data](../questions/walksheds/how-does-walksheds-use-os-connect-data.md)

### `explain-accessmap`

**Example query:** How is AccessMap different from Walksheds?

**Retrieve these pages:**

- [how-is-accessmap-different-from-walksheds](../questions/support/how-is-accessmap-different-from-walksheds.md)

### `support-stop-planning`

**Example query:** How can OS-CONNECT and Walksheds help with bus stop placement or access analysis?

**Retrieve these pages:**

- [how-can-os-connect-and-walksheds-support-bus-stop-planning](../questions/support/how-can-os-connect-and-walksheds-support-bus-stop-planning.md)

### `support-event-accessibility`

**Example query:** How can OS-CONNECT support FIFA or major-event accessibility planning?

**Retrieve these pages:**

- [can-os-connect-support-fifa-or-major-event-accessibility-planning](../questions/os-connect/can-os-connect-support-fifa-or-major-event-accessibility-planning.md)

### `support-school-access`

**Example query:** How can pedestrian accessibility data be used around schools and transit stops?

**Retrieve these pages:**

- [can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations](../questions/os-connect/can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations.md)

### `explain-community-mapping-pathways`

**Example query:** A local mapping group wants to restart sidewalk mapping. What support can TCAT offer?

**Retrieve these pages:**

- [can-tcat-help-set-up-a-sidewalk-mapping-project-in-the-osm-us-tasking-manager](../questions/os-connect/can-tcat-help-set-up-a-sidewalk-mapping-project-in-the-osm-us-tasking-manager.md)

### `explain-tasking-manager-status`

**Example query:** What happened to the old MapWith.ai Tasking Manager, and what should we recommend now?

**Retrieve these pages:**

- [what-happened-to-the-older-opensidewalks-mapwith-ai-tasking-manager-workflow](../questions/os-connect/what-happened-to-the-older-opensidewalks-mapwith-ai-tasking-manager-workflow.md)

### `onboard-new-mappers`

**Example query:** What beginner materials should we share with sidewalk mappers?

**Retrieve these pages:**

- [what-training-materials-are-available-for-new-sidewalk-mappers](../questions/os-connect/what-training-materials-are-available-for-new-sidewalk-mappers.md)

### `decide-mapping-priorities`

**Example query:** How should a community decide where to start mapping sidewalks?

**Retrieve these pages:**

- [how-should-communities-decide-which-areas-to-map-first](../questions/os-connect/how-should-communities-decide-which-areas-to-map-first.md)

### `explain-data-quality-expectations`

**Example query:** When can volunteer-contributed sidewalk data become useful for agency planning?

**Retrieve these pages:**

- [what-makes-community-mapped-sidewalk-data-usable-for-agency-workflows](../questions/os-connect/what-makes-community-mapped-sidewalk-data-usable-for-agency-workflows.md)

### `refer-to-mappy-hours`

**Example query:** When is Mappy Hours the right next step?

**Retrieve these pages:**

- [when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support](../questions/support/when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support.md)

### `decide-direct-support-vs-office-hours`

**Example query:** When should staff answer directly instead of referring someone to Mappy Hours?

**Retrieve these pages:**

- [when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support](../questions/support/when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support.md)

### `draft-professional-support-response`

**Example query:** Draft a professional response to an agency partner asking about OS-CONNECT correction timelines.

**Suggested pattern:** `answer-known-operational`

**Retrieve these pages:**

- [how-long-do-corrections-take-to-appear-in-a-public-release](../questions/os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md)

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

- [who-owns-follow-up-when-a-partner-asks-a-question-that-crosses-tools-or-teams](../questions/support/who-owns-follow-up-when-a-partner-asks-a-question-that-crosses-tools-or-teams.md)

### `propose-next-step`

**Example query:** A partner has a practical use case but we do not yet know the answer. What should we say next?

**Suggested pattern:** `answer-when-uncertain`

**Retrieve these pages:**

- [what-should-staff-do-when-they-do-not-know-the-answer-to-a-partner-s-question](../questions/support/what-should-staff-do-when-they-do-not-know-the-answer-to-a-partner-s-question.md)

## What This Does Not Mean

- Not an exhaustive list of every user utterance.
- Not automated routing without human review for high-risk topics.

## How To Use This

Index this page and linked question pages together. At query time, classify to an intent ID, fetch related pages, then apply a support answer pattern when drafting.

## Assistant Guidance

Prefer intents over raw keyword search for cross-tool questions. If no intent fits, abstain and escalate per [Assistant abstention](../policies/assistant-abstention.md).

## Related Concepts

- [Support answer patterns](../workflows/support-answer-patterns.md)
- [Helpline FAQ backlog](../backlog/helpline-faq-backlog.md)

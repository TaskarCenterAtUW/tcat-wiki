---
title: Helpline & Question Board FAQ backlog
slug: helpline-faq-backlog
doc_type: workflow
products:
  - OS-CONNECT
  - AccessMap
  - Walksheds
  - TDEI
audiences:
  - planner
  - jurisdiction
  - public
topics:
  - helpline
  - backlog
risk_level: low
authority_level: draft
review_status: draft
last_reviewed: "2026-05-18"
retrieval_priority: high
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - This backlog replaces product manuals or operational runbooks.
related_pages:
  - assistant/intents/support-intents.md
  - assistant/workflows/support-answer-patterns.md
  - assistant/index.md
---

# Helpline & Question Board FAQ backlog

## Short Answer

This page tracks practical FAQ and support questions from the Question Board and helpline, maps them to assistant pages, and links to RAG **intents** and **answer patterns** for staff retrieval.

## Significance

Partners ask workflow questions—downloads, corrections, ArcGIS, GTFS Pathways, OSM tagging, Mappy Hours—that differ from abstract product FAQs. This backlog aligns human authoring with RAG grounding.

## Top 10 priority FAQ (author first)

1. [What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?](../questions/support/what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap.md)
2. [Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?](../questions/support/which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis.md)
3. [How do I report an error in OS-CONNECT data?](../questions/os-connect/how-do-i-report-an-error-in-os-connect-data.md)
4. [What happens after I submit an issue report?](../questions/os-connect/what-happens-after-i-submit-an-issue-report.md)
5. [How long do corrections take to appear in a public release?](../questions/os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md)
6. [Can agencies submit bulk corrections or priority areas for review?](../questions/os-connect/can-agencies-submit-bulk-corrections-or-priority-areas-for-review.md)
7. [How is OS-CONNECT different from GTFS Pathways?](../questions/support/how-is-os-connect-different-from-gtfs-pathways.md)
8. [How can OS-CONNECT and Walksheds support bus stop planning?](../questions/support/how-can-os-connect-and-walksheds-support-bus-stop-planning.md)
9. [How should separately mapped sidewalks be associated with street names in OSM?](../questions/os-connect/how-should-separately-mapped-sidewalks-be-associated-with-street-names-in-osm.md)
10. [When should partners be referred to Mappy Hours versus direct technical support?](../questions/support/when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support.md)

## Coverage summary

- **Total helpline FAQ entries:** 97
- **External-user questions:** 86
- **Staff / support operations:** 11
- **RAG intents:** 35 → [Support intents](../intents/support-intents.md)
- **Answer patterns:** 5 → [Support answer patterns](../workflows/support-answer-patterns.md)

Machine-readable source: `scripts/data/helpline_faq_backlog.json`. Regenerate stubs: `python scripts/build_helpline_backlog.py`.

## New question areas (May 2026 helpline)

Compared to the original 300-question batch, this backlog adds emphasis on:

- **Ecosystem clarity** (TDEI vs OS-CONNECT vs OpenSidewalks vs OSM vs AccessMap vs Walksheds vs GTFS)
- **Downloads & OSW format** (files, edges/nodes, OSW vs OSM export)
- **Issue reporting lifecycle** (viewer reports, review, releases, bulk corrections)
- **GTFS Pathways** (vs OS-CONNECT, pathways.txt, missing pathways)
- **OSM sidewalk street-name tagging** (for trip-planning vendors)
- **Community mapping & Mappy Hours** (Tasking Manager, training, referrals)
- **Support operations** (contacts, tone, uncertainty, cross-team ownership)

Cross-product pages live under [Support & helpline questions](../questions/support/index.md).

## External FAQ (all)

- [Are Sound Transit or other agencies publishing GTFS Pathways data?](../questions/support/are-sound-transit-or-other-agencies-publishing-gtfs-pathways-data.md)
- [Can OS-CONNECT data be used in ArcGIS?](../questions/os-connect/can-i-use-this-in-arcgis-or-qgis.md)
- [Can OS-CONNECT generate GTFS Pathways data?](../questions/os-connect/can-os-connect-generate-gtfs-pathways-data.md)
- [Can OS-CONNECT support ADA transition planning?](../questions/os-connect/can-os-connect-be-used-for-ada-transition-planning.md)
- [Can OS-CONNECT support FIFA or major-event accessibility planning?](../questions/os-connect/can-os-connect-support-fifa-or-major-event-accessibility-planning.md)
- [Can OS-CONNECT support bus stop planning?](../questions/os-connect/can-os-connect-support-bus-stop-planning.md)
- [Can OS-CONNECT support capital planning?](../questions/os-connect/can-os-connect-support-capital-planning.md)
- [Can OS-CONNECT support pedestrian access analysis around schools, clinics, grocery stores, and other destinations?](../questions/os-connect/can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations.md)
- [Can OS-CONNECT support service planning and reliability analysis?](../questions/os-connect/can-os-connect-support-service-planning-and-reliability-analysis.md)
- [Can TCAT help set up a sidewalk-mapping project in the OSM US Tasking Manager?](../questions/os-connect/can-tcat-help-set-up-a-sidewalk-mapping-project-in-the-osm-us-tasking-manager.md)
- [Can Walksheds be joined with census, crash, or internal agency datasets?](../questions/walksheds/can-walksheds-be-joined-with-census-crash-or-internal-agency-datasets.md)
- [Can agencies or community groups attend Mappy Hours?](../questions/support/can-agencies-or-community-groups-attend-mappy-hours.md)
- [Can agencies provide their own sidewalk or curb-ramp data for integration?](../questions/os-connect/can-agencies-provide-their-own-sidewalk-or-curb-ramp-data-for-integration.md)
- [Can agencies submit bulk corrections or priority areas for review?](../questions/os-connect/can-agencies-submit-bulk-corrections-or-priority-areas-for-review.md) ⭐
- [Can an agency submit a batch of known corrections instead of reporting one issue at a time?](../questions/os-connect/can-an-agency-submit-a-batch-of-known-corrections-instead-of-reporting-one-issue-at-a-time.md)
- [Can mapping volunteers contribute data that agencies can use?](../questions/os-connect/can-mapping-volunteers-contribute-data-that-agencies-can-use.md)
- [Do reported issues automatically update the public dataset?](../questions/os-connect/do-reported-issues-automatically-update-the-public-dataset.md)
- [Does a correction update OS-CONNECT, OpenStreetMap, TDEI, or all of them?](../questions/os-connect/does-a-correction-update-os-connect-openstreetmap-tdei-or-all-of-them.md)
- [How are agency-submitted corrections validated?](../questions/os-connect/how-are-agency-submitted-corrections-validated.md)
- [How are corrections tracked across releases?](../questions/os-connect/how-are-corrections-tracked-across-releases.md)
- [How can I tell whether a GTFS feed includes pathways.txt?](../questions/support/how-can-i-tell-whether-a-gtfs-feed-includes-pathways-txt.md)
- [How can OS-CONNECT and Walksheds support bus stop planning?](../questions/support/how-can-os-connect-and-walksheds-support-bus-stop-planning.md) ⭐
- [How can Walksheds help analyze access to bus stops?](../questions/walksheds/how-can-walksheds-help-analyze-access-to-bus-stops.md)
- [How can an agency confirm that a submitted correction was incorporated?](../questions/os-connect/how-can-an-agency-confirm-that-a-submitted-correction-was-incorporated.md)
- [How can trip planners use sidewalk street-name tags to produce better walking instructions?](../questions/os-connect/how-can-trip-planners-use-sidewalk-street-name-tags-to-produce-better-walking-instructions.md)
- [How do I import OS-CONNECT / OSW GeoJSON into ArcGIS?](../questions/os-connect/how-do-i-import-os-connect-osw-geojson-into-arcgis.md)
- [How do I know whether a dataset is authoritative?](../questions/support/how-do-i-know-whether-a-dataset-is-authoritative.md)
- [How do I know whether a dataset is current?](../questions/tdei/how-do-i-know-whether-a-dataset-is-current.md)
- [How do I report an error in OS-CONNECT data?](../questions/os-connect/how-do-i-report-an-error-in-os-connect-data.md) ⭐
- [How do OpenSidewalks mapping efforts relate to local community mapping groups such as Maptime LA?](../questions/os-connect/how-do-opensidewalks-mapping-efforts-relate-to-local-community-mapping-groups-such-as-maptime-la.md)
- [How does AccessMap consume OpenSidewalks or OS-CONNECT data?](../questions/accessmap/how-does-accessmap-consume-opensidewalks-or-os-connect-data.md)
- [How does Walksheds use OS-CONNECT data?](../questions/walksheds/how-does-walksheds-use-os-connect-data.md)
- [How is AccessMap different from Walksheds?](../questions/support/how-is-accessmap-different-from-walksheds.md)
- [How is GTFS Pathways different from OS-CONNECT?](../questions/support/how-is-gtfs-pathways-different-from-os-connect.md)
- [How is OS-CONNECT different from GTFS Pathways?](../questions/support/how-is-os-connect-different-from-gtfs-pathways.md) ⭐
- [How long do corrections take to appear in a public release?](../questions/os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md) ⭐
- [How long does it take for a correction to appear in a public release?](../questions/os-connect/how-long-does-it-take-for-a-correction-to-appear-in-a-public-release.md)
- [How should agencies treat OS-CONNECT data in planning workflows when known errors exist?](../questions/os-connect/how-should-agencies-treat-os-connect-data-in-planning-workflows-when-known-errors-exist.md)
- [How should an agency cite OS-CONNECT or TDEI data?](../questions/support/how-should-an-agency-cite-os-connect-or-tdei-data.md)
- [How should communities decide which areas to map first?](../questions/os-connect/how-should-communities-decide-which-areas-to-map-first.md)
- [How should separately mapped sidewalks be associated with street names in OSM?](../questions/os-connect/how-should-separately-mapped-sidewalks-be-associated-with-street-names-in-osm.md) ⭐
- [How should separately mapped sidewalks be associated with street names in OpenStreetMap?](../questions/os-connect/how-should-separately-mapped-sidewalks-be-associated-with-street-names-in-openstreetmap.md)
- [Is OS-CONNECT the same as OpenStreetMap data?](../questions/os-connect/how-is-os-connect-different-from-openstreetmap.md)
- [What are edges and nodes in the OSW download?](../questions/tdei/what-are-edges-and-nodes-in-the-osw-download.md)
- [What attributes are included for sidewalks, crossings, curb ramps, and related pedestrian features?](../questions/os-connect/what-attributes-are-included-for-sidewalks-crossings-curb-ramps-and-related-pedestrian-features.md)
- [What does "released dataset" mean in TDEI?](../questions/tdei/what-does-released-dataset-mean-in-tdei.md)
- [What does it mean that OS-CONNECT uses the OpenSidewalks schema?](../questions/os-connect/what-does-it-mean-that-os-connect-uses-the-opensidewalks-schema.md)
- [What does it mean to route using accessibility preferences?](../questions/accessmap/what-does-it-mean-to-route-using-accessibility-preferences.md)
- [What files are included in an OSW download?](../questions/tdei/what-files-are-included-in-an-osw-download.md)
- [What happened to the older OpenSidewalks / MapWith.ai Tasking Manager workflow?](../questions/os-connect/what-happened-to-the-older-opensidewalks-mapwith-ai-tasking-manager-workflow.md)
- [What happens after I submit an issue report?](../questions/os-connect/what-happens-after-i-submit-an-issue-report.md) ⭐
- [What information should agencies include when reporting a data issue?](../questions/os-connect/what-information-should-agencies-include-when-reporting-a-data-issue.md)
- [What is AccessMap?](../questions/accessmap/what-is-accessmap.md)
- [What is GTFS Pathways?](../questions/accessmap/what-is-gtfs-pathways.md)
- [What is OS-CONNECT?](../questions/os-connect/what-is-os-connect.md)
- [What is OpenSidewalks?](../questions/os-connect/what-is-opensidewalks.md)
- [What is TDEI?](../questions/tdei/what-is-tdei.md)
- [What is a project group in TDEI?](../questions/tdei/what-is-a-project-group-in-tdei.md)
- [What is a walkshed?](../questions/walksheds/what-is-a-walkshed.md)
- [What is the difference between TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex?](../questions/support/ecosystem-differences-tdei-os-connect-opensidewalks-osm-accessmap-walksheds-gtfs.md)
- [What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?](../questions/support/what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap.md) ⭐
- [What is the difference between a pedestrian walkshed and a wheelchair-user walkshed?](../questions/walksheds/what-is-the-difference-between-a-pedestrian-walkshed-and-a-wheelchair-user-walkshed.md)
- [What is the difference between downloading OSW format and OSM format?](../questions/tdei/what-is-the-difference-between-downloading-osw-format-and-osm-format.md)
- [What is the difference between street:name=* and is_sidepath:of:name=*?](../questions/os-connect/what-is-the-difference-between-street-name-and-is-sidepath-of-name.md)
- [What is the relationship between pedestrian paths in OpenStreetMap and GTFS Pathways?](../questions/support/what-is-the-relationship-between-pedestrian-paths-in-openstreetmap-and-gtfs-pathways.md)
- [What kinds of errors should be reported through the OS-CONNECT Viewer?](../questions/os-connect/what-kinds-of-errors-should-be-reported-through-the-os-connect-viewer.md)
- [What makes community-mapped sidewalk data usable for agency workflows?](../questions/os-connect/what-makes-community-mapped-sidewalk-data-usable-for-agency-workflows.md)
- [What quality checks are needed before community-mapped data can support planning or routing?](../questions/os-connect/what-quality-checks-are-needed-before-community-mapped-data-can-support-planning-or-routing.md)
- [What should I do if a dataset appears mislabeled or downloads the wrong file?](../questions/tdei/what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file.md)
- [What should agencies do if GTFS Pathways data are missing but pedestrian data exist in OSM or OS-CONNECT?](../questions/support/what-should-agencies-do-if-gtfs-pathways-data-are-missing-but-pedestrian-data-exist-in-osm-or-os-connect.md)
- [What should agencies do if they need a correction sooner than the next public release?](../questions/os-connect/what-should-agencies-do-if-they-need-a-correction-sooner-than-the-next-public-release.md)
- [What should mappers do when a sidewalk is separated from the road geometry?](../questions/os-connect/what-should-mappers-do-when-a-sidewalk-is-separated-from-the-road-geometry.md)
- [What should trip-planning vendors do when OSM pedestrian paths do not include street names?](../questions/os-connect/what-should-trip-planning-vendors-do-when-osm-pedestrian-paths-do-not-include-street-names.md)
- [What training materials are available for new sidewalk mappers?](../questions/os-connect/what-training-materials-are-available-for-new-sidewalk-mappers.md)
- [What travel profiles are available in Walksheds?](../questions/walksheds/what-travel-profiles-are-available-in-walksheds.md)
- [When should partners be referred to Mappy Hours versus direct technical support?](../questions/support/when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support.md) ⭐
- [When should someone be referred to Mappy Hours versus receiving direct support?](../questions/support/when-should-someone-be-referred-to-mappy-hours-versus-receiving-direct-support.md)
- [Where are OpenSidewalks attribute definitions documented?](../questions/os-connect/where-are-opensidewalks-attribute-definitions-documented.md)
- [Where do I download OS-CONNECT data?](../questions/tdei/where-do-i-download-os-connect-data.md)
- [Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?](../questions/support/which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis.md) ⭐
- [Which dataset should I use if I need pedestrian walkway data for planning?](../questions/support/which-dataset-should-i-use-if-i-need-pedestrian-walkway-data-for-planning.md)
- [Which dataset should I use if I need transit-station pathway data?](../questions/support/which-dataset-should-i-use-if-i-need-transit-station-pathway-data.md)
- [Which sidewalk-to-street-name tagging pattern is currently recommended?](../questions/os-connect/which-sidewalk-to-street-name-tagging-pattern-is-currently-recommended.md)
- [Who reviews submitted issue reports?](../questions/os-connect/who-reviews-submitted-issue-reports.md)
- [Why do street names matter for walking directions?](../questions/os-connect/why-do-street-names-matter-for-walking-directions.md)
- [Why might a test dataset appear in the portal?](../questions/tdei/why-might-a-test-dataset-appear-in-the-portal.md)

## Staff / support operations

- [How should staff distinguish current functionality from future plans?](../questions/support/how-should-staff-distinguish-current-functionality-from-future-plans.md)
- [How should staff explain uncertainty without sounding evasive?](../questions/support/how-should-staff-explain-uncertainty-without-sounding-evasive.md)
- [How should staff introduce related tools without making the answer feel like a sales pitch?](../questions/support/how-should-staff-introduce-related-tools-without-making-the-answer-feel-like-a-sales-pitch.md)
- [What language should staff use when a question requires internal verification?](../questions/support/what-language-should-staff-use-when-a-question-requires-internal-verification.md)
- [What response time should external partners expect?](../questions/support/what-response-time-should-external-partners-expect.md)
- [What should staff avoid saying in external technical-support emails?](../questions/support/what-should-staff-avoid-saying-in-external-technical-support-emails.md)
- [What should staff do when they do not know the answer to a partner's question?](../questions/support/what-should-staff-do-when-they-do-not-know-the-answer-to-a-partner-s-question.md)
- [Who owns follow-up when a partner asks a question that crosses tools or teams?](../questions/support/who-owns-follow-up-when-a-partner-asks-a-question-that-crosses-tools-or-teams.md)
- [Who should external partners contact for OS-CONNECT data questions?](../questions/support/who-should-external-partners-contact-for-os-connect-data-questions.md)
- [Who should external partners contact for OpenSidewalks mapping questions?](../questions/support/who-should-external-partners-contact-for-opensidewalks-mapping-questions.md)
- [Who should external partners contact for TDEI support?](../questions/support/who-should-external-partners-contact-for-tdei-support.md)

## Assistant Guidance

Author the top 10 and the issue-reporting cluster first. Use [support answer patterns](../workflows/support-answer-patterns.md) when drafting replies. Route ambiguous queries via [support intents](../intents/support-intents.md). Do not ingest TODO stubs into production RAG without review filters.

## Related Concepts

- [Support intents](../intents/support-intents.md)
- [Support answer patterns](../workflows/support-answer-patterns.md)
- [Assistant Knowledge Base](../index.md)

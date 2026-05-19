#!/usr/bin/env python3
"""
Build helpline FAQ backlog JSON and generate net-new question stubs.

Reads/writes scripts/data/helpline_faq_backlog.json and creates missing pages under
docs/assistant/questions/ without overwriting existing files.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "scripts" / "data" / "helpline_faq_backlog.json"
ASSISTANT = ROOT / "docs" / "assistant"

# Import slug helpers from existing generator
sys.path.insert(0, str(ROOT / "scripts"))
from generate_assistant_questions_300 import (  # noqa: E402
    PRODUCT_FOR_FOLDER,
    build_page,
    risk_level_for,
    slugify,
)

PRIORITY_FAQ = [
    "What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?",
    "Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?",
    "How do I report an error in OS-CONNECT data?",
    "What happens after I submit an issue report?",
    "How long do corrections take to appear in a public release?",
    "Can agencies submit bulk corrections or priority areas for review?",
    "How is OS-CONNECT different from GTFS Pathways?",
    "How can OS-CONNECT and Walksheds support bus stop planning?",
    "How should separately mapped sidewalks be associated with street names in OSM?",
    "When should partners be referred to Mappy Hours versus direct technical support?",
]

FAQ_QUESTIONS: list[dict] = [
    # Ecosystem & definitions
    {"q": "What is TDEI?", "folder": "tdei", "priority": "external", "topics": ["tdei-overview"]},
    {"q": "What is OS-CONNECT?", "folder": "os-connect", "priority": "external", "topics": ["os-connect-overview"], "existing_path": "assistant/questions/os-connect/what-is-os-connect.md"},
    {"q": "What is OpenSidewalks?", "folder": "os-connect", "priority": "external", "topics": ["opensidewalks-overview"]},
    {"q": "What is the difference between TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex?", "folder": "support", "priority": "external", "topics": ["ecosystem", "overview"]},
    {"q": "What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?", "folder": "support", "priority": "external", "topics": ["ecosystem", "overview"]},
    {"q": "Is OS-CONNECT the same as OpenStreetMap data?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "data-model"], "existing_path": "assistant/questions/os-connect/how-is-os-connect-different-from-openstreetmap.md"},
    {"q": "What does it mean that OS-CONNECT uses the OpenSidewalks schema?", "folder": "os-connect", "priority": "external", "topics": ["opensidewalks", "schema"]},
    # Dataset selection & download
    {"q": "Which dataset should I use if I need pedestrian walkway data for planning?", "folder": "support", "priority": "external", "topics": ["dataset-selection", "planning"]},
    {"q": "Which dataset should I use if I need transit-station pathway data?", "folder": "support", "priority": "external", "topics": ["dataset-selection", "gtfs-pathways"]},
    {"q": "Where do I download OS-CONNECT data?", "folder": "tdei", "priority": "external", "topics": ["downloads", "tdei"], "existing_path": "assistant/questions/tdei/where-do-i-download-os-connect-data.md"},
    {"q": "What is the difference between downloading OSW format and OSM format?", "folder": "tdei", "priority": "external", "topics": ["downloads", "formats"]},
    {"q": "What files are included in an OSW download?", "folder": "tdei", "priority": "external", "topics": ["downloads", "formats", "osw"]},
    {"q": "What are edges and nodes in the OSW download?", "folder": "tdei", "priority": "external", "topics": ["downloads", "routing-graph", "osw"]},
    {"q": "Can OS-CONNECT data be used in ArcGIS?", "folder": "os-connect", "priority": "external", "topics": ["gis", "arcgis"], "existing_path": "assistant/questions/os-connect/can-i-use-this-in-arcgis-or-qgis.md"},
    {"q": "Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?", "folder": "support", "priority": "external", "topics": ["dataset-selection", "arcgis", "planning"]},
    {"q": "How do I import OS-CONNECT / OSW GeoJSON into ArcGIS?", "folder": "os-connect", "priority": "external", "topics": ["gis", "arcgis", "imports"]},
    {"q": "What attributes are included for sidewalks, crossings, curb ramps, and related pedestrian features?", "folder": "os-connect", "priority": "external", "topics": ["attributes", "schema"]},
    {"q": "Where are OpenSidewalks attribute definitions documented?", "folder": "os-connect", "priority": "external", "topics": ["opensidewalks", "schema", "documentation"]},
    {"q": "How should an agency cite OS-CONNECT or TDEI data?", "folder": "support", "priority": "external", "topics": ["citation", "governance"]},
    {"q": "How do I know whether a dataset is current?", "folder": "tdei", "priority": "external", "topics": ["data-freshness", "releases"]},
    {"q": "How do I know whether a dataset is authoritative?", "folder": "support", "priority": "external", "topics": ["authority", "governance"]},
    {"q": "What does \"released dataset\" mean in TDEI?", "folder": "tdei", "priority": "external", "topics": ["releases", "tdei"]},
    {"q": "What is a project group in TDEI?", "folder": "tdei", "priority": "external", "topics": ["tdei", "project-groups"]},
    {"q": "Why might a test dataset appear in the portal?", "folder": "tdei", "priority": "external", "topics": ["tdei", "releases", "testing"]},
    {"q": "What should I do if a dataset appears mislabeled or downloads the wrong file?", "folder": "tdei", "priority": "external", "topics": ["tdei", "support", "downloads"]},
    # Issue reporting & corrections
    {"q": "How do I report an error in OS-CONNECT data?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "issue-reporting"]},
    {"q": "What kinds of errors should be reported through the OS-CONNECT Viewer?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "data-viewer"]},
    {"q": "What happens after I submit an issue report?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "issue-reporting"]},
    {"q": "Do reported issues automatically update the public dataset?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "releases"]},
    {"q": "Who reviews submitted issue reports?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "stewardship"]},
    {"q": "How long does it take for a correction to appear in a public release?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "releases"]},
    {"q": "How long do corrections take to appear in a public release?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "releases"]},
    {"q": "Can an agency submit a batch of known corrections instead of reporting one issue at a time?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "agencies"]},
    {"q": "Can agencies submit bulk corrections or priority areas for review?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "agencies"]},
    {"q": "Can agencies provide their own sidewalk or curb-ramp data for integration?", "folder": "os-connect", "priority": "external", "topics": ["stewardship", "agencies"]},
    {"q": "What information should agencies include when reporting a data issue?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "agencies"]},
    {"q": "How are agency-submitted corrections validated?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "validation"]},
    {"q": "Does a correction update OS-CONNECT, OpenStreetMap, TDEI, or all of them?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "stewardship", "openstreetmap"]},
    {"q": "How are corrections tracked across releases?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "releases"]},
    {"q": "How can an agency confirm that a submitted correction was incorporated?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "agencies"]},
    {"q": "What should agencies do if they need a correction sooner than the next public release?", "folder": "os-connect", "priority": "external", "topics": ["feedback", "releases"]},
    {"q": "How should agencies treat OS-CONNECT data in planning workflows when known errors exist?", "folder": "os-connect", "priority": "external", "topics": ["planning", "data-quality"]},
    # Planning use cases
    {"q": "Can OS-CONNECT support bus stop planning?", "folder": "os-connect", "priority": "external", "topics": ["planning", "transit", "bus-stops"]},
    {"q": "How can OS-CONNECT and Walksheds support bus stop planning?", "folder": "support", "priority": "external", "topics": ["planning", "transit", "walksheds"]},
    {"q": "Can OS-CONNECT support service planning and reliability analysis?", "folder": "os-connect", "priority": "external", "topics": ["planning", "transit"]},
    {"q": "Can OS-CONNECT support capital planning?", "folder": "os-connect", "priority": "external", "topics": ["planning", "capital"]},
    {"q": "Can OS-CONNECT support ADA transition planning?", "folder": "os-connect", "priority": "external", "topics": ["ada", "planning"], "existing_path": "assistant/questions/os-connect/can-os-connect-be-used-for-ada-transition-planning.md"},
    {"q": "Can OS-CONNECT support FIFA or major-event accessibility planning?", "folder": "os-connect", "priority": "external", "topics": ["planning", "events"]},
    {"q": "Can OS-CONNECT support pedestrian access analysis around schools, clinics, grocery stores, and other destinations?", "folder": "os-connect", "priority": "external", "topics": ["planning", "destinations"]},
    # Walksheds & AccessMap
    {"q": "What is a walkshed?", "folder": "walksheds", "priority": "external", "topics": ["walksheds-overview"], "existing_path": "assistant/questions/walksheds/what-is-a-walkshed.md"},
    {"q": "How does Walksheds use OS-CONNECT data?", "folder": "walksheds", "priority": "external", "topics": ["walksheds", "os-connect"]},
    {"q": "What is the difference between a pedestrian walkshed and a wheelchair-user walkshed?", "folder": "walksheds", "priority": "external", "topics": ["walksheds", "profiles"]},
    {"q": "What travel profiles are available in Walksheds?", "folder": "walksheds", "priority": "external", "topics": ["walksheds", "profiles"]},
    {"q": "How can Walksheds help analyze access to bus stops?", "folder": "walksheds", "priority": "external", "topics": ["walksheds", "transit", "bus-stops"]},
    {"q": "Can Walksheds be joined with census, crash, or internal agency datasets?", "folder": "walksheds", "priority": "external", "topics": ["walksheds", "gis", "analysis"]},
    {"q": "What is AccessMap?", "folder": "accessmap", "priority": "external", "topics": ["accessmap-overview"], "existing_path": "assistant/questions/accessmap/what-is-accessmap.md"},
    {"q": "How is AccessMap different from Walksheds?", "folder": "support", "priority": "external", "topics": ["accessmap", "walksheds"]},
    {"q": "How does AccessMap consume OpenSidewalks or OS-CONNECT data?", "folder": "accessmap", "priority": "external", "topics": ["accessmap", "os-connect"]},
    {"q": "What does it mean to route using accessibility preferences?", "folder": "accessmap", "priority": "external", "topics": ["accessmap", "routing"]},
    # GTFS Pathways
    {"q": "What is GTFS Pathways?", "folder": "accessmap", "priority": "external", "topics": ["gtfs-pathways"], "existing_path": "assistant/questions/accessmap/what-is-gtfs-pathways.md"},
    {"q": "How is GTFS Pathways different from OS-CONNECT?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "os-connect"]},
    {"q": "How is OS-CONNECT different from GTFS Pathways?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "os-connect"]},
    {"q": "Can OS-CONNECT generate GTFS Pathways data?", "folder": "os-connect", "priority": "external", "topics": ["gtfs-pathways", "exports"]},
    {"q": "Are Sound Transit or other agencies publishing GTFS Pathways data?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "publishers"]},
    {"q": "How can I tell whether a GTFS feed includes pathways.txt?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "validation"]},
    {"q": "What is the relationship between pedestrian paths in OpenStreetMap and GTFS Pathways?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "openstreetmap"]},
    {"q": "What should agencies do if GTFS Pathways data are missing but pedestrian data exist in OSM or OS-CONNECT?", "folder": "support", "priority": "external", "topics": ["gtfs-pathways", "planning"]},
    # OSM mapping & street names
    {"q": "How should separately mapped sidewalks be associated with street names in OpenStreetMap?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "mapping", "street-names"]},
    {"q": "How should separately mapped sidewalks be associated with street names in OSM?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "mapping", "street-names"]},
    {"q": "What is the difference between street:name=* and is_sidepath:of:name=*?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "tagging"]},
    {"q": "Which sidewalk-to-street-name tagging pattern is currently recommended?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "tagging"]},
    {"q": "Why do street names matter for walking directions?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "routing", "navigation"]},
    {"q": "How can trip planners use sidewalk street-name tags to produce better walking instructions?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "routing", "vendors"]},
    {"q": "What should mappers do when a sidewalk is separated from the road geometry?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "mapping"]},
    {"q": "What should trip-planning vendors do when OSM pedestrian paths do not include street names?", "folder": "os-connect", "priority": "external", "topics": ["openstreetmap", "vendors"]},
    # Community mapping
    {"q": "How do OpenSidewalks mapping efforts relate to local community mapping groups such as Maptime LA?", "folder": "os-connect", "priority": "external", "topics": ["community", "mapping"]},
    {"q": "Can TCAT help set up a sidewalk-mapping project in the OSM US Tasking Manager?", "folder": "os-connect", "priority": "external", "topics": ["community", "tasking-manager"]},
    {"q": "What happened to the older OpenSidewalks / MapWith.ai Tasking Manager workflow?", "folder": "os-connect", "priority": "external", "topics": ["community", "tasking-manager"]},
    {"q": "What training materials are available for new sidewalk mappers?", "folder": "os-connect", "priority": "external", "topics": ["community", "training"]},
    {"q": "How should communities decide which areas to map first?", "folder": "os-connect", "priority": "external", "topics": ["community", "mapping"]},
    {"q": "Can mapping volunteers contribute data that agencies can use?", "folder": "os-connect", "priority": "external", "topics": ["community", "stewardship"]},
    {"q": "What makes community-mapped sidewalk data usable for agency workflows?", "folder": "os-connect", "priority": "external", "topics": ["community", "data-quality"]},
    {"q": "What quality checks are needed before community-mapped data can support planning or routing?", "folder": "os-connect", "priority": "external", "topics": ["community", "validation"]},
    {"q": "Can agencies or community groups attend Mappy Hours?", "folder": "support", "priority": "external", "topics": ["mappy-hours", "community"]},
    {"q": "When should someone be referred to Mappy Hours versus receiving direct support?", "folder": "support", "priority": "external", "topics": ["mappy-hours", "support"]},
    {"q": "When should partners be referred to Mappy Hours versus direct technical support?", "folder": "support", "priority": "external", "topics": ["mappy-hours", "support"]},
    # Support operations (staff-facing, still in public KB with care)
    {"q": "Who should external partners contact for TDEI support?", "folder": "support", "priority": "support", "topics": ["contacts", "tdei"]},
    {"q": "Who should external partners contact for OS-CONNECT data questions?", "folder": "support", "priority": "support", "topics": ["contacts", "os-connect"]},
    {"q": "Who should external partners contact for OpenSidewalks mapping questions?", "folder": "support", "priority": "support", "topics": ["contacts", "opensidewalks"]},
    {"q": "Who owns follow-up when a partner asks a question that crosses tools or teams?", "folder": "support", "priority": "support", "topics": ["contacts", "ownership"]},
    {"q": "What response time should external partners expect?", "folder": "support", "priority": "support", "topics": ["support", "sla"]},
    {"q": "What should staff do when they do not know the answer to a partner's question?", "folder": "support", "priority": "support", "topics": ["support", "escalation"]},
    {"q": "What language should staff use when a question requires internal verification?", "folder": "support", "priority": "support", "topics": ["support", "communication"]},
    {"q": "What should staff avoid saying in external technical-support emails?", "folder": "support", "priority": "support", "topics": ["support", "communication"]},
    {"q": "How should staff explain uncertainty without sounding evasive?", "folder": "support", "priority": "support", "topics": ["support", "communication"]},
    {"q": "How should staff distinguish current functionality from future plans?", "folder": "support", "priority": "support", "topics": ["support", "roadmap"]},
    {"q": "How should staff introduce related tools without making the answer feel like a sales pitch?", "folder": "support", "priority": "support", "topics": ["support", "communication"]},
]

INTENTS = [
    {"id": "explain-ecosystem", "example_query": "A partner is confused about TDEI, OS-CONNECT, OpenSidewalks, and OSM. Give a short explanation of how they relate.", "related_slugs": ["what-is-the-difference-between-tdei-os-connect-opensidewalks-and-openstreetmap", "what-is-tdei", "what-is-os-connect", "what-is-opensidewalks"]},
    {"id": "recommend-dataset", "example_query": "An agency wants pedestrian walkway data for bus stop planning in ArcGIS. Which dataset and format should we recommend?", "related_slugs": ["which-dataset-and-format-should-an-agency-use-for-pedestrian-walkway-data-in-arcgis", "which-dataset-should-i-use-if-i-need-pedestrian-walkway-data-for-planning"]},
    {"id": "guide-download", "example_query": "A user downloaded the wrong file from TDEI. How should we help them find the correct released OS-CONNECT dataset?", "related_slugs": ["what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file", "where-do-i-download-os-connect-data", "what-does-released-dataset-mean-in-tdei"]},
    {"id": "explain-osw-format", "example_query": "What does an OSW download contain, and how do edges and nodes map to sidewalks, crossings, and curb ramps?", "related_slugs": ["what-files-are-included-in-an-osw-download", "what-are-edges-and-nodes-in-the-osw-download"]},
    {"id": "support-arcgis-use", "example_query": "How should I explain importing OS-CONNECT GeoJSON into ArcGIS?", "related_slugs": ["how-do-i-import-os-connect-osw-geojson-into-arcgis", "can-os-connect-data-be-used-in-arcgis"]},
    {"id": "handle-mislabeled-datasets", "example_query": "A public dataset appears mislabeled or points to a wrong download. What should support staff say and do?", "related_slugs": ["what-should-i-do-if-a-dataset-appears-mislabeled-or-downloads-the-wrong-file"]},
    {"id": "explain-issue-reporting", "example_query": "A user found a railroad track incorrectly marked as a walkway. How should they report it?", "related_slugs": ["how-do-i-report-an-error-in-os-connect-data", "what-kinds-of-errors-should-be-reported-through-the-os-connect-viewer"]},
    {"id": "explain-correction-lifecycle", "example_query": "How long does it take for submitted corrections to appear in OS-CONNECT?", "related_slugs": ["how-long-do-corrections-take-to-appear-in-a-public-release", "what-happens-after-i-submit-an-issue-report"]},
    {"id": "distinguish-release-from-review", "example_query": "Does submitting an issue immediately change the public dataset?", "related_slugs": ["do-reported-issues-automatically-update-the-public-dataset"]},
    {"id": "handle-bulk-corrections", "example_query": "An agency has many known sidewalk errors. Should they submit them individually or coordinate a structured review?", "related_slugs": ["can-agencies-submit-bulk-corrections-or-priority-areas-for-review"]},
    {"id": "validate-authority", "example_query": "A partner asks whether this is the authoritative pedestrian dataset for their jurisdiction. What can we safely say?", "related_slugs": ["how-do-i-know-whether-a-dataset-is-authoritative"]},
    {"id": "explain-gtfs-pathways-relationship", "example_query": "A transit agency asks whether OS-CONNECT is a substitute for GTFS Pathways.", "related_slugs": ["how-is-os-connect-different-from-gtfs-pathways"]},
    {"id": "check-gtfs-pathways-availability", "example_query": "How can someone tell whether a GTFS feed includes pathways.txt?", "related_slugs": ["how-can-i-tell-whether-a-gtfs-feed-includes-pathways-txt"]},
    {"id": "support-trip-planning-vendors", "example_query": "A trip planner has poor walking directions because sidewalks lack street-name references. What should we explain?", "related_slugs": ["what-should-trip-planning-vendors-do-when-osm-pedestrian-paths-do-not-include-street-names"]},
    {"id": "explain-osm-sidewalk-naming-tags", "example_query": "What are street:name and is_sidepath:of:name, and when should they be used?", "related_slugs": ["what-is-the-difference-between-street-name-and-is-sidepath-of-name"]},
    {"id": "recommend-osm-tagging-practice", "example_query": "Which tag should we recommend for associating sidewalks with street names?", "related_slugs": ["which-sidewalk-to-street-name-tagging-pattern-is-currently-recommended"]},
    {"id": "connect-mapping-to-routing", "example_query": "Why does sidewalk tagging matter for navigation instructions?", "related_slugs": ["why-do-street-names-matter-for-walking-directions"]},
    {"id": "explain-walksheds", "example_query": "How should support staff explain Walksheds to a transit planner?", "related_slugs": ["what-is-a-walkshed", "how-does-walksheds-use-os-connect-data"]},
    {"id": "explain-accessmap", "example_query": "How is AccessMap different from Walksheds?", "related_slugs": ["how-is-accessmap-different-from-walksheds"]},
    {"id": "support-stop-planning", "example_query": "How can OS-CONNECT and Walksheds help with bus stop placement or access analysis?", "related_slugs": ["how-can-os-connect-and-walksheds-support-bus-stop-planning"]},
    {"id": "support-event-accessibility", "example_query": "How can OS-CONNECT support FIFA or major-event accessibility planning?", "related_slugs": ["can-os-connect-support-fifa-or-major-event-accessibility-planning"]},
    {"id": "support-school-access", "example_query": "How can pedestrian accessibility data be used around schools and transit stops?", "related_slugs": ["can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations"]},
    {"id": "explain-community-mapping-pathways", "example_query": "A local mapping group wants to restart sidewalk mapping. What support can TCAT offer?", "related_slugs": ["can-tcat-help-set-up-a-sidewalk-mapping-project-in-the-osm-us-tasking-manager"]},
    {"id": "explain-tasking-manager-status", "example_query": "What happened to the old MapWith.ai Tasking Manager, and what should we recommend now?", "related_slugs": ["what-happened-to-the-older-opensidewalks-mapwith-ai-tasking-manager-workflow"]},
    {"id": "onboard-new-mappers", "example_query": "What beginner materials should we share with sidewalk mappers?", "related_slugs": ["what-training-materials-are-available-for-new-sidewalk-mappers"]},
    {"id": "decide-mapping-priorities", "example_query": "How should a community decide where to start mapping sidewalks?", "related_slugs": ["how-should-communities-decide-which-areas-to-map-first"]},
    {"id": "explain-data-quality-expectations", "example_query": "When can volunteer-contributed sidewalk data become useful for agency planning?", "related_slugs": ["what-makes-community-mapped-sidewalk-data-usable-for-agency-workflows"]},
    {"id": "refer-to-mappy-hours", "example_query": "When is Mappy Hours the right next step?", "related_slugs": ["when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support"]},
    {"id": "decide-direct-support-vs-office-hours", "example_query": "When should staff answer directly instead of referring someone to Mappy Hours?", "related_slugs": ["when-should-partners-be-referred-to-mappy-hours-versus-direct-technical-support"]},
    {"id": "draft-professional-support-response", "example_query": "Draft a professional response to an agency partner asking about OS-CONNECT correction timelines.", "related_slugs": ["how-long-do-corrections-take-to-appear-in-a-public-release"], "uses_pattern": "answer-known-operational"},
    {"id": "soften-support-tone", "example_query": "Rewrite this support email to be warmer but less casual and more technically precise.", "uses_pattern": "answer-when-uncertain"},
    {"id": "manage-uncertainty", "example_query": "Rewrite this answer so it does not overstate what we know.", "uses_pattern": "answer-when-uncertain"},
    {"id": "preserve-relationship-continuity", "example_query": "Draft a reply to a partner who is reconnecting after several months about a paused sidewalk-mapping project.", "uses_pattern": "reconnect-prior-collaborator"},
    {"id": "identify-ownership", "example_query": "This question crosses data, portal, and mapping workflows. Who should own the follow-up?", "related_slugs": ["who-owns-follow-up-when-a-partner-asks-a-question-that-crosses-tools-or-teams"]},
    {"id": "propose-next-step", "example_query": "A partner has a practical use case but we do not yet know the answer. What should we say next?", "related_slugs": ["what-should-staff-do-when-they-do-not-know-the-answer-to-a-partner-s-question"], "uses_pattern": "answer-when-uncertain"},
]

PATTERNS = [
    {"id": "answer-known-operational", "title": "Answer a known operational question", "structure": "direct answer → brief explanation → link if needed → next step"},
    {"id": "answer-when-uncertain", "title": "Answer when uncertain", "structure": "state what is known → state what is not confirmed → who is checking → interim guidance"},
    {"id": "respond-to-data-error", "title": "Respond to a data error", "structure": "thank them → likely issue category → reporting path → review lifecycle → structured follow-up for agency-scale issues"},
    {"id": "explain-tool-without-overselling", "title": "Explain a tool without overselling it", "structure": "connect to stated use case → what it does → current limitations → next step"},
    {"id": "reconnect-prior-collaborator", "title": "Reconnect with a prior collaborator", "structure": "acknowledge prior context → recognize current update → answer current question → concrete way to continue"},
]


def index_existing() -> dict[str, str]:
    by_slug: dict[str, str] = {}
    for p in ASSISTANT.rglob("*.md"):
        if p.name == "index.md":
            continue
        rel = p.relative_to(ROOT / "docs").as_posix()
        by_slug[p.stem] = rel
    return by_slug


def resolve_paths(faq: list[dict], by_slug: dict[str, str]) -> list[dict]:
    seen: set[str] = set()
    out = []
    for row in faq:
        q = row["q"]
        slug = slugify(q)
        path = row.get("existing_path")
        if not path:
            path = by_slug.get(slug)
        if path and slug not in seen:
            seen.add(slug)
            out.append({**row, "slug": slug, "existing_path": path, "status": "existing"})
        elif slug in seen:
            continue
        else:
            seen.add(slug)
            out.append({**row, "slug": slug, "existing_path": None, "status": "new"})
    return out


def generate_stubs(faq: list[dict], by_slug: dict[str, str]) -> int:
    created = 0
    support_index: list[tuple[str, str]] = []
    for row in faq:
        if row.get("status") != "new":
            continue
        folder = row["folder"]
        slug = row["slug"]
        title = row["q"]
        topics = row["topics"]
        if folder == "support":
            out_dir = ASSISTANT / "questions" / "support"
            products = ["OS-CONNECT", "AccessMap", "Walksheds", "TDEI"]
        elif folder == "policies":
            out_dir = ASSISTANT / "policies"
            products = PRODUCT_FOR_FOLDER["policies"]
        else:
            out_dir = ASSISTANT / "questions" / folder
            products = PRODUCT_FOR_FOLDER.get(folder, ["OS-CONNECT"])
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{slug}.md"
        if out_path.exists():
            continue
        risk = risk_level_for(title, topics)
        body = build_page(title, slug, folder if folder != "support" else "os-connect", topics, risk, "high")
        if folder == "support":
            # patch products for support folder
            body = body.replace(
                "products:\n  - OS-CONNECT",
                "products:\n  - OS-CONNECT\n  - AccessMap\n  - Walksheds\n  - TDEI",
                1,
            )
        out_path.write_text(body, encoding="utf-8")
        by_slug[slug] = out_path.relative_to(ROOT / "docs").as_posix()
        row["existing_path"] = by_slug[slug]
        row["status"] = "stub_created"
        created += 1
        if folder == "support":
            support_index.append((slug, title))
    if support_index:
        write_support_index(support_index, by_slug)
    return created


def write_support_index(items: list[tuple[str, str]], by_slug: dict[str, str]) -> None:
    base = ASSISTANT / "questions" / "support"
    lines = [
        "---",
        'title: "Support & helpline questions"',
        "---",
        "",
        "# Support & helpline questions",
        "",
        "Cross-product questions from the Question Board and helpline. "
        "Prioritize [Helpline FAQ backlog](../backlog/helpline-faq-backlog.md) for authoring order.",
        "",
    ]
    for slug, title in sorted(items, key=lambda x: x[1].lower()):
        lines.append(f"- [{title}]({slug}.md)")
    (base / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    by_slug = index_existing()
    faq = resolve_paths(FAQ_QUESTIONS, by_slug)
    created = generate_stubs(faq, by_slug)
    # refresh paths after generation
    faq = resolve_paths(FAQ_QUESTIONS, index_existing())

    payload = {
        "version": 1,
        "source": "Question Board and helpline (May 2026)",
        "priority_faq": PRIORITY_FAQ,
        "faq_questions": faq,
        "intents": INTENTS,
        "patterns": PATTERNS,
    }
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    existing = sum(1 for r in faq if r["status"] == "existing")
    new = sum(1 for r in faq if r["status"] == "new")
    stubbed = sum(1 for r in faq if r["status"] == "stub_created")
    print(f"Wrote {DATA_PATH}", file=sys.stderr)
    print(f"FAQ entries: {len(faq)} (existing={existing}, new_pending={new}, stubs_created={stubbed})", file=sys.stderr)
    print(f"Created {created} new stub pages.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

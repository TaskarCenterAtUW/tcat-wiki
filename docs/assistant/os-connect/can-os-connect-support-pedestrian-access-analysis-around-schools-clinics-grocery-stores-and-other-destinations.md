---
title: "Can OS-CONNECT support pedestrian access analysis around schools, clinics, grocery stores, and other destinations?"
tags:
    - Assistant
slug: can-os-connect-support-pedestrian-access-analysis-around-schools-clinics-grocery-stores-and-other-destinations
doc_type: question
products:
    - OS-CONNECT
    - Walksheds
    - AccessMap
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - planning
    - destinations
    - pedestrian-access
    - walksheds
    - accessibility-analysis
    - destinations
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - OS-CONNECT proves that a destination is accessible
        - OS-CONNECT guarantees current field conditions
        - walkshed results are equivalent to ADA compliance
        - straight-line distance is sufficient for pedestrian access analysis
related_pages:
    - walksheds
    - accessmap-routing
    - accessibility-islands
    - connected-pedestrian-graph
    - data-freshness
    - ada-compliance-boundaries
---

# Can OS-CONNECT support pedestrian access analysis around schools, clinics, grocery stores, and other destinations?

## Short Answer

Yes. OS-CONNECT can support pedestrian access analysis around destinations such as schools, clinics, grocery stores, transit stops, parks, civic buildings, and other essential services when it is used with tools such as Walksheds, AccessMap, and related TDEI workflows.

OS-CONNECT provides a connected pedestrian network that can be used to evaluate how people may reach destinations through sidewalks, crossings, curb ramps, paths, slopes, and other pedestrian infrastructure features.

This kind of analysis is stronger than simple distance-based analysis because it can account for the actual pedestrian network and accessibility-related barriers. However, results should be interpreted as planning and decision-support outputs, not as guarantees of accessibility, safety, ADA compliance, or current field conditions.

## Significance

Pedestrian access to everyday destinations is a core question for transportation equity, accessibility planning, public health, and local infrastructure investment.

Many traditional access analyses use straight-line buffers, such as "within a quarter mile of a school" or "within a half mile of a grocery store." Those buffers can be misleading because they do not show whether a person can actually travel through the pedestrian network.

Two homes may be the same distance from a clinic, school, grocery store, or bus stop, but have very different access conditions depending on:
- whether sidewalks are connected,
- whether crossings exist,
- whether curb ramps are present,
- whether slopes are passable for a given mobility profile,
- whether barriers such as stairs or raised curbs interrupt the route,
- and whether the available path requires difficult or unsafe crossings.

OS-CONNECT makes it possible to ask more operational questions, such as:
- Which homes or blocks are actually reachable from a school?
- Which neighborhoods are cut off from a clinic by missing crossings?
- Which grocery stores are reachable for a manual wheelchair profile within a given travel budget?
- Which infrastructure gaps most affect access to transit stops or essential services?
- How would access change if a missing crossing, curb ramp, or sidewalk connection were added?

This is important because access is not only about proximity. It is about whether the pedestrian environment supports usable movement.

## What This Means

OS-CONNECT can be used as the network foundation for destination-based pedestrian access analysis.

In practice, destination analysis can combine:
- OS-CONNECT pedestrian network data,
- destination points such as schools, clinics, grocery stores, parks, libraries, or transit stops,
- Walksheds analysis,
- AccessMap routing profiles,
- local GIS data,
- community observations,
- and field validation.

The Walksheds tool can calculate the area reachable from a selected origin point or destination point within a given travel time or cost budget. The result reflects characteristics of the pedestrian network, including sidewalks, crossings, slopes, curbs, stairs, and other barriers when those data are available.

This allows planners and advocates to evaluate access around destinations using network-based reachability rather than straight-line distance.

For example, a Walksheds analysis can help show:
- how far someone can travel from a school using the pedestrian network,
- which nearby blocks are not reachable because of missing connections,
- how access differs for different mobility profiles,
- whether a destination is isolated by poor crossing connectivity,
- and how proposed infrastructure changes could improve reachable area.

AccessMap can complement this analysis by supporting route-level interpretation. It can help users understand why an accessibility-aware route may be longer than a typical shortest path and how route preferences or mobility profiles affect routing.

## What This Does Not Mean

OS-CONNECT destination analysis does not mean:
- the destination is fully accessible,
- every route to the destination is safe,
- the pedestrian environment is ADA compliant,
- data reflects current field conditions,
- missing attributes should be interpreted as absence of barriers,
- or a walkshed result is a legal accessibility determination.

OS-CONNECT should not be treated as a substitute for:
- field verification,
- engineering review,
- ADA transition planning requirements,
- local asset inventories,
- community validation,
- or current construction and maintenance information.

A destination may appear reachable in a network analysis but still present real-world barriers that are not fully represented in the data, such as:
- temporary construction,
- poor surface condition,
- snow or debris,
- blocked sidewalks,
- missing tactile information,
- signal timing issues,
- lighting or personal safety concerns,
- or unrecorded curb ramp details.

Similarly, a destination may appear poorly connected because of missing or outdated data. In those cases, the result should be treated as a prompt for review rather than a final conclusion.

## How To Use This

Use OS-CONNECT destination analysis as a planning, screening, and prioritization workflow.

A typical workflow is:

1. Identify destinations of interest.
   Examples include schools, clinics, grocery stores, libraries, parks, transit stops, civic buildings, shelters, senior centers, or community facilities.

2. Select the relevant OS-CONNECT or TDEI pedestrian dataset.

3. Use Walksheds to calculate reachable areas around selected destinations or origins.

4. Select appropriate mobility profiles or travel assumptions.
   Different profiles may produce different reachable areas.

5. Compare results across destinations, neighborhoods, or populations.

6. Identify gaps, such as missing crossings, disconnected sidewalks, steep routes, inaccessible curb conditions, or isolated pedestrian network segments.

7. Use AccessMap or related routing tools to inspect route-level implications.

8. Validate high-priority findings with local knowledge, field review, or community input.

9. Use findings to support planning workflows such as:
   - Safe Routes to School,
   - ADA transition planning support,
   - transit stop access review,
   - pedestrian safety planning,
   - Vision Zero analysis,
   - Complete Streets prioritization,
   - clinic or health access analysis,
   - grocery access analysis,
   - park access analysis,
   - and grant applications.

The best use of OS-CONNECT is not to say "this place is accessible" or "this place is inaccessible" in a final sense. The better use is to identify where pedestrian network conditions may support or restrict access, then prioritize review, investment, and community validation.

## Example

A jurisdiction wants to understand pedestrian access to grocery stores and clinics for residents who rely on walking, rolling, or transit.

The planning team selects the relevant OS-CONNECT pedestrian dataset and adds destination points for:
- grocery stores,
- clinics,
- bus stops,
- senior housing,
- and community service locations.

Using Walksheds, the team calculates reachable areas around each destination for a general pedestrian profile and a manual wheelchair profile.

The results show that several neighborhoods are close to a clinic by straight-line distance but are not well connected through the pedestrian network. The analysis reveals missing crossings, disconnected sidewalk segments, and curb-related barriers that reduce access for the wheelchair profile.

The team then uses these results to:
- identify priority locations for field validation,
- compare access across neighborhoods,
- discuss improvements with community members,
- support Safe Routes to School or public health access planning,
- and prepare a clearer infrastructure investment case.

The analysis does not certify that any route is ADA compliant. It provides a grounded planning view of pedestrian access conditions and where further review is needed.

## Assistant Guidance

When answering this question, the assistant should say that OS-CONNECT can support destination-based pedestrian access analysis when combined with tools such as Walksheds, AccessMap, and appropriate destination datasets.

The assistant should emphasize that:
- OS-CONNECT supports network-based analysis, not just distance buffers,
- Walksheds can show reachable areas based on pedestrian network conditions,
- different mobility profiles may produce different access results,
- destination analysis can support planning and prioritization,
- and results should be validated before operational or legal conclusions are made.

The assistant should avoid claiming that:
- OS-CONNECT proves accessibility,
- a destination is ADA compliant,
- routes are currently safe,
- data is complete or current,
- or analysis results can replace field validation.

If the assistant does not know:
- which dataset was used,
- when it was last updated,
- which destination layer was used,
- which mobility profile was selected,
- or whether field validation occurred,

it should qualify the answer and avoid definitive claims.

The assistant should encourage users to interpret the analysis as decision support for planning, review, and stewardship rather than as a final accessibility determination.

## Related Concepts

- Walksheds
- AccessMap Routing
- Connected Pedestrian Graph
- Accessibility Islands
- Mobility Profiles
- Destination-Based Access Analysis
- Data Freshness
- Field Validation
- ADA Compliance Boundaries
- Safe Routes to School
- Transit Stop Access
- Complete Streets
- Community Validation

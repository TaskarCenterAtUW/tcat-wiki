<!-- @format -->

# OSM US Tasking Manager Project Settings

## Description

**Database**: OpenStreetMap

**Status**: Published

**Priority**: Low

### Name

**Format**:

"`<EventTag>` | `<Neighborhood>`, `<City>`, `<State`, `<Country>`: `<Topic>` | `<OpenSidewalksTag>`"

**Example 1**:

    #MappyNewYear2026 | Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks

**Example 2**:

    Downtown, Austin, TX, US: Crossings | #OpenSidewalks

**Example 3**:

    #MaptimeES | Eixample, Barcelona, ES: Sidewalks | #OpenSidewalks

### Short description

**Format**:

"Map `<Topic>` in `<Location` to `<Impact>`."

**Example 1**:

    Map sidewalks, crossings, and curbs in Olympia, WA, US to improve pedestrian navigation data.

### Description

**Example 1**:

    **Olympia, WA, US: Pedestrian Infrastructure | #OpenSidewalks**

    This project focuses on mapping pedestrian infrastructure in Olympia, WA as part of the OpenSidewalks initiative. Contributors will map sidewalks, crossings, and curbs to create a complete, routable pedestrian network.

    This data enables accessibility-focused routing applications like [AccessMap](https://www.accessmap.app/) to provide safe, personalized pedestrian directions which are especially important for people with mobility challenges or who are blind/low-vision.

    **Mapping Guide:** [https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/](https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/)

    No prior mapping experience required - join the [OpenSidewalks Mappers team](https://tasks.openstreetmap.us/teams/27/membership/) to get started!
    Due date: _none_

## Instructions

### Changeset comment

**Example 1**:

    | Olympia, WA, US: Pedestrian Infrastructure | #OpenSidewalks

### Detailed instructions

## What to Map

**Example 1**:

    Map the **pedestrian network** in your task area:

    1. **Crossings** - Lines across streets where pedestrians cross
    2. **Curbs** - Points at crossing endpoints (lowered, raised, or flush)
    3. **Sidewalks** - Lines along the center of pedestrian paths
    4. **Connectors** - Short lines linking sidewalks to curbs

    ## Quick Tagging Reference

    **Essential tags:**

    - Crossings (line): `highway=footway` + `footway=crossing` + `crossing:markings=yes`/`no`
    - Crossings (point): `highway=crossing` + `crossing:markings=yes`/`no`
    - Curbs (point): `barrier=kerb` + `kerb=lowered`/`raised`/`flush`
    - Sidewalks (line): `highway=footway` + `footway=sidewalk`
    - Connectors (line): `highway=footway` + `footway=sidewalk` + (optional) `crossing_link=yes`

    ## Key Rules

    - Draw sidewalks along the **center** of the path
    - Crossing midpoints must **share a node** with the road
    - **Connect** sidewalks to curbs with short connector footways
    - Use street-level imagery (Bing Streetside, Mapillary) to verify curb types

    ## Full Guide

    For complete instructions with images and examples, visit:
    **[https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/](https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/)**

### Per task instructions

**Example 1**:

    Map all sidewalks, crossings, and curbs in this task area.

    **Priority:** Crossings & Curbs → Sidewalks & Connectors

    **Essential tags:**

    - Crossings (line): `highway=footway` + `footway=crossing` + `crossing:markings=yes`/`no`
    - Crossings (point): `highway=crossing` + `crossing:markings=yes`/`no`
    - Curbs (point): `barrier=kerb` + `kerb=lowered`/`raised`/`flush`
    - Sidewalks (line): `highway=footway` + `footway=sidewalk`
    - Connectors (line): `highway=footway` + `footway=sidewalk` + (optional) `crossing_link=yes`

    **Remember:** Create a fully-connected network to support routing!

    **Full guide:** [[https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/](https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/)](<https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/](https://taskarcenteratuw.github.io/tcat-wiki/events/olympia-connected/mapping-guide/)>)

## Metadata

**Difficulty**: Moderate
**Types of mapping**: Other
**iD editor presets**: _none_
**Additional iD URL parameters**: _none_
**Organization**: OpenSidewalks
**Campaign**: _none_
**OSMCha filter ID**: _none_

## Priority areas

_none_

## Imagery

**Imagery**: Bing
**Required license**: _none_

## Permissions

**Mapping permissions**: Only team members
**Validation permissions**: Only team members
**Teams**:
**Filter by**: OpenSidewalks
OpenSidewalks - Project Managers: _Project Manager_
OpenSidewalks - Validators: _Validator_
OpenSidewalks - Mappers: _Mapper_
**Privacy**: _no_

## Settings

**Default language**: English (en)
**Editors for mapping:**
Rapid: _yes_
iD Editor: _yes_
JOSM: _yes_
Potlatch 2: _no_
Field Papers: _no_
**Editors for validation:**
Rapid: _yes_
iD Editor: _yes_
JOSM: _yes_
Potlatch 2: _no_
Field Papers: _no_
**Enforce random task selection**: no
**Enable RapiD Power User Features**: no

## Actions

_none_

## Custom Editor

**Name**: _none_
**Description**: _none_
**URL**: _none_

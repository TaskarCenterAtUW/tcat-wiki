---
title: Welcome
---

<!-- @format -->

## Welcome to the TCAT Wiki!

This site explains how to use the open-source transportation accessibility **tools** and **data** developed by the [Taskar Center for Accessible Technology](https://tcat.cs.washington.edu/) (TCAT), especially [OS-CONNECT](os-connect/index.md) (Washington State's connected pedestrian network dataset) and the [TDEI](tdei/index.md) (the infrastructure that stores and serves that data).

---

### What's Your Goal?

| If you want to… | Use                                                                                                  |
| :-------------- | :--------------------------------------------------------------------------------------------------- |
| **View**        | [OS-CONNECT Data Viewer](os-connect/data-viewer/index.md) — a view-only map; no GIS required         |
| **Download**    | [TDEI Portal](tdei/portal/index.md) — manage accounts, API keys, and access controls                 |
| **Plan**        | [Walksheds](walksheds/index.md) — scenario planning, project proposal evaluation, and prioritization |
| **Route**       | [AccessMap](accessmap/index.md) — a public routing app, no portal required                           |

---

### User Journeys

Choose your path: each one starts with the simplest document and then offers deeper options.

??? abstract "I want to use AccessMap: find and share accessible, customized pedestrian routes"

    **Get Started:** View the [AccessMap user manual](accessmap/user-manual/index.md).

??? abstract "I work for a jurisdiction or agency: view pedestrian infrastructure and decide what to do next"

    **Get Started:** [View the data](os-connect/data-viewer/user-manual/index.md) and [read a Jurisdiction Snapshot](os-connect/qa-qc/user-manual/index.md).

??? abstract "I want to import existing sidewalk, curb ramp, bus stop, or other data into the TDEI"

    **Get Started:** Review the [Curb Points in TDEI tutorial](tdei/portal/tutorial/curb-points-in-tdei.md).

??? abstract "I want to contribute as a mapper: map sidewalks, crossings, and curbs"

    **Get Started:** Follow the [Mapping for OSW in OSM tutorial](opensidewalks/tasking-manager/tutorial/osw-in-osmustm/index.md), and get started in your area or choose a [Tasking Manager project](opensidewalks/tasking-manager/project-list.md).

??? abstract "I want to improve the data: validate OS-CONNECT data and report issues"

    **Get Started:** [Open the OS-CONNECT Data Viewer](os-connect/data-viewer/index.md), then [report an issue](os-connect/data-viewer/user-manual/feedback.md).

??? abstract "I want to use OS-CONNECT data for planning, equity, and accessibility work"

    **Get Started:** [Read the OS-CONNECT QA/QC reports](os-connect/qa-qc/user-manual/index.md) and [use Walksheds](walksheds/index.md) for scenario planning and prioritization.

??? abstract "I want to develop or research with the data: download data, use APIs, and work with schemas"

    **Get Started:** Follow the [OS-CONNECT download guide](tdei/portal/tutorial/download-os-connect.md) and review the [OpenSidewalks Schema documentation](opensidewalks/schema/index.md).

---

### Key Takeaways

If you remember only three things, remember these:

**[OS-CONNECT](os-connect/index.md) is the dataset** — It is a connected pedestrian network for Washington State (sidewalks, crossings, curb ramps, and related features) in the [OpenSidewalks schema](opensidewalks/schema/index.md), organized so it can be used for routing and analysis.

**[TDEI](tdei/index.md) is the platform** — It is where data can be accessed for downloads and APIs, and where tools like [AccessMap](accessmap/index.md), [Walksheds](walksheds/index.md), [AVIV ScoutRoute](aviv-scoutroute/index.md), and [Workspaces](workspaces/index.md) connect to the data.

**[AccessMap](accessmap/index.md) is the router** — It uses OpenSidewalks Schema-formatted data to provide custom accessible pedestrian routing without requiring specialized tools.

---

### Projects

**[OS-CONNECT](os-connect/index.md)** — Washington State connected pedestrian network dataset. No standalone public source repository is currently listed for the dataset.

**[TDEI](tdei/index.md)** — Platform infrastructure for storing, serving, and integrating transportation accessibility data. Public components include [TDEI Tools](https://github.com/TaskarCenterAtUW/tdei-tools), [Workspaces frontend](https://github.com/TaskarCenterAtUW/workspaces-frontend), and [Workspaces backend](https://github.com/TaskarCenterAtUW/workspaces-backend).

**[OpenSidewalks](opensidewalks/index.md)** — The data standard/schema used to represent pedestrian networks as a connected graph. The public [OpenSidewalks Schema repository](https://github.com/OpenSidewalks/OpenSidewalks-Schema) contains the schema source.

**[Workspaces](workspaces/index.md)** — Tools for creating and maintaining OSW datasets (via editors like [Rapid](rapid/index.md) and [AVIV ScoutRoute](aviv-scoutroute/index.md)). Public components include the [frontend](https://github.com/TaskarCenterAtUW/workspaces-frontend), [backend](https://github.com/TaskarCenterAtUW/workspaces-backend), and [deployment stack](https://github.com/TaskarCenterAtUW/workspaces-stack).

**[AccessMap](accessmap/index.md)** — Accessible multimodal routing and trip planning. See the public [AccessMap repository](https://github.com/TaskarCenterAtUW/AccessMap).

**[Walksheds](walksheds/index.md)** — Analysis of access to destinations using the pedestrian network. No standalone public source repository is currently listed for the tool.

**[AVIV ScoutRoute](aviv-scoutroute/index.md)** — Mobile app for adding data into the existing pedestrian map. AVIV ScoutRoute enables everyone to make structured, clear, and direct contributions of surveyed data to enhance it or keep it up to date. See the public [GoInfoGame repository](https://github.com/OpenSidewalks/GoInfoGame) and [iOS repository](https://github.com/TaskarCenterAtUW/GoInfoGame-iOS).

**[Rapid](rapid/index.md)** — OpenStreetMap-based editor used by Workspaces. See the public [Rapid repository](https://github.com/meta/Rapid) and [Workspaces Rapid integration repository](https://github.com/TaskarCenterAtUW/workspaces-rapid).

_Additional TCAT projects are listed on the [TCAT website](https://tcat.cs.washington.edu/current-projects/)._

### Source Code, Branches, and Contributions

The public repositories linked above use repository-specific branch structures. Most use `main` as the default branch; the Workspaces frontend uses `develop`, and other repositories may retain release, staging, or feature branches. Check each repository's branch list and contribution guidance before opening a change.

External contributions are accepted through issues and pull requests in public repositories, subject to each project's maintainer review and contribution guidance. The TCAT Wiki itself welcomes minor external contributions; see the [contribution guide](../CONTRIBUTING.md).

---

### Quick Concepts

New to this? If you are unfamiliar with some of this terminology, start with these short explanations to learn the concepts in less than 5 minutes:

??? question "Points of Interest (POIs)"

    A **point of interest** (POI) is a specific, identifiable location that is relevant to pedestrians or travelers, such as a transit stop, park entrance, business, public facility, or other amenity. In the context of TCAT projects, POIs are used alongside pedestrian network data to analyze access to destinations and services.

??? question "Connected Networks"

    A **connected network** is a graph of pedestrian infrastructure — sidewalks, crossings, curb ramps, and other paths — where all elements are linked as Nodes, Edges, and Zones forming a complete, traversable network. This is in contrast to disconnected or partial datasets where features exist in isolation.

    **Why this matters:**

    - **Routing** — A connected network enables turn-by-turn pedestrian navigation and accessibility-focused trip planning (as in [AccessMap](accessmap/index.md)), because every path segment connects to the next.
    - **Analysis** — Connectivity allows for network-level analyses (such as [walksheds](walksheds/index.md)), enabling gap detection and equity assessments — computations that require understanding how infrastructure elements relate to one another.

??? question "Walksheds"

    A **walkshed** is the area reachable via a specified mode of transport from a given location within a specified travel time or distance, considering the actual pedestrian network. Unlike a simple radius, a walkshed accounts for real-world path connectivity, barriers, and infrastructure conditions. The [Walksheds](walksheds/index.md) tool uses pedestrian network data to compute and visualize these areas, enabling analysis of access to amenities and services.

    :octicons-arrow-right-24: [Learn more](walksheds/index.md)

??? question "Routing Profiles"

    A **routing profile** is a set of preferences and constraints that customize how a pedestrian route is calculated. For example, a routing profile may specify maximum acceptable incline, preference for curb ramps, or avoidance of unpaved surfaces. Tools like [AccessMap](accessmap/index.md) use routing profiles to generate personalized, accessibility-aware directions based on individual needs.

    :octicons-arrow-right-24: [Learn more](accessmap/index.md)

---

### Tutorials, User Manuals, and Guides

Looking for step-by-step instructions? Start with our full **[Guides List](guides-list/index.md)** or try ++ctrl+k++ **Search**!

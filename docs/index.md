---
title: Welcome
---

<!-- @format -->

## Welcome to the TCAT Wiki!

This site explains how to use the open-source transportation accessibility **tools** and **data** developed by the [Taskar Center for Accessible Technology](https://tcat.cs.washington.edu/) (TCAT), especially [OS-CONNECT](os-connect/index.md) (Washington State's connected pedestrian network dataset) and the [TDEI](tdei/index.md) (the infrastructure that stores and serves that data).

---

### Projects

**[OpenSidewalks](opensidewalks/index.md)** — An open data standard for pedestrian networks.

**[TDEI](tdei/index.md)** — The Transportation Data Exchange Initiative: infrastructure for collecting, storing, maintaining, and sharing transportation data.

**[OS-CONNECT](os-connect/index.md)** — A connected pedestrian network dataset covering 320+ jurisdictions in Washington State.

**[Workspaces](workspaces/index.md)** — A platform for creating, editing, and maintaining OSW datasets, using the web-based [Rapid](rapid/index.md) editor or the [AVIV ScoutRoute](aviv-scoutroute/index.md) mobile app.

**[AccessMap](accessmap/index.md)** — Trip planning and customizable accessibility-focused multimodal routing.

**[Walksheds](walksheds/index.md)** — Tool for analyzing pedestrian infrastructure and access to amenities.

**[Events](events/index.md)** — Mapping events and our weekly [Mappy Hours](events/oswmh/index.md).

_Additional TCAT projects can be found [on the TCAT website](https://tcat.cs.washington.edu/current-projects/)._

---

### Quick Concepts

??? question "What is OS-CONNECT?"

    **OS-CONNECT** (OpenSidewalks COnsistent Network for accessible Navigation and Equitable Connectivity through Transit) is a comprehensive, high-resolution, connected pedestrian network dataset for Washington State. Created under the directive of the Washington State Legislature, OS-CONNECT provides detailed sidewalk infrastructure data across 320+ cities and counties, supporting Washington's goals around transportation equity, safety, and accessibility.

    [:octicons-arrow-right-24: Learn more](os-connect/index.md)

??? question "What is the TDEI?"

    The **Transportation Data Exchange Initiative** (TDEI) is a shared, standardized framework for transportation data that enables seamless integration across mobility systems. The TDEI provides infrastructure for collecting, storing, maintaining, and sharing open data about sidewalks, transit paths, and on-demand transit services, laying the groundwork for more effective transportation planning and innovation.

    [:octicons-arrow-right-24: Learn more](tdei/index.md)

??? question "What is OSW / OSW Schema?"

    **OpenSidewalks** (OSW) is an initiative led by TCAT to provide a comprehensive, accessibility-forward specification for mapping sidewalks and related pedestrian infrastructure. The **OpenSidewalks Schema** is the open data standard that promotes an explicit network (graph) model. Its primary features are defined as connected Nodes (points) and Edges (lines) representing a traversable, graph-analyzable pedestrian network of sidewalks, street crossings, and other paths, along with data representing potential barriers such as stairs and raised curbs.

    [:octicons-arrow-right-24: Learn more](opensidewalks/index.md)

??? question "What is a Connected Network?"

    A **connected network** is a graph of pedestrian infrastructure such as sidewalks, crossings, curb ramps, and other paths where all elements are linked as Nodes, Edges, and Zones forming a complete, traversable network. This is in contrast to disconnected or partial datasets where features exist in isolation.

    **Why this matters:**

    - **Routing** — A connected network enables turn-by-turn pedestrian navigation and accessibility-focused trip planning (as in [AccessMap](accessmap/index.md)), because every path segment connects to the next.
    - **Analysis** — Connectivity allows for network-level analyses (such as [walksheds](walksheds/index.md)), enabling gap detection and equity assessments, computations that require understanding how infrastructure elements relate to one another.

??? question "What is a POI?"

    A **Point of Interest** (POI) is a specific, identifiable location that is relevant to pedestrians or travelers, such as a transit stop, park entrance, business, public facility, or other amenity. In the context of TCAT projects, POIs are used alongside pedestrian network data to analyze access to destinations and services.

??? question "What is a Walkshed?"

    A **walkshed** is the area reachable via a specified mode of transport from a given location within a specified travel time or distance, considering the actual pedestrian network. Unlike a simple radius, a walkshed accounts for real-world path connectivity, barriers, and infrastructure conditions. The [TDEI Walksheds](walksheds/index.md) tool uses pedestrian network data to compute and visualize these areas, enabling analysis of access to amenities and services.

    [:octicons-arrow-right-24: Learn more](walksheds/index.md)

??? question "What is a Routing Profile?"

    A **routing profile** is a set of preferences and constraints that customize how a pedestrian route is calculated. For example, a routing profile may specify maximum acceptable incline, preference for curb ramps, or avoidance of unpaved surfaces. Tools like [AccessMap](accessmap/index.md) use routing profiles to generate personalized, accessibility-aware directions based on individual needs.

    [:octicons-arrow-right-24: Learn more](accessmap/index.md)

---

### Resources

- **[Guides List](guides-list/index.md)** — User manuals, tutorials, and technical documentation

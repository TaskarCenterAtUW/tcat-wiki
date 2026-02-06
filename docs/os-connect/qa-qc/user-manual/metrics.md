---
title: OS-CONNECT QA/QC Report Subsections in Detail
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## OS-CONNECT QA/QC Report Subsections in Detail

This guide covers the details of each OS-CONNECT QA/QC report subsection and metric.

---

Referenced are the three QA/QC reports for the Bellevue, Everett, and Goldendale jurisdictions.

### Tag Completion Subreport

Metric Category: _Intrinsic_

This section quantifies the attribute completeness of essential pedestrian infrastructure features. A Python script processes the edge GeoJSON and outputs both summary statistics and a derived GeoJSON highlighting incomplete features.

Metrics reported:

- Percentage of edges with complete tags for: sidewalk, crossing, footway
- Frequency of specific tags such as: length, surface, incline, width, etc.

These measures do not validate tag accuracy but rather reflect whether necessary tags are present. Completeness indicators can inform priorities for further data collection, especially when preparing data for downstream applications like accessibility modeling or routing.

### Walkshed Metrics Subreport

Metric Category: _Extrinsic_

Walkshed metrics assess the effective accessible reach of a jurisdiction's pedestrian network under two user profiles:

- Unconstrained pedestrian
- Manual wheelchair user

Procedure:

POIs (e.g., community centers, transit stops, libraries) are retrieved from OpenStreetMap using the Overpass API and from Overture using the Overture API.

Walksheds are generated around these POIs and merged to form a unified coverage map for each profile.

A Python script calculates metrics such as:

- Total reachable path length (in meters)
- Count of crossings, curbs, marked curbs, and lowered curbs

Metrics are visualized in both tabular and spatial formats, including convex hulls representing disconnected "accessibility islands." These metrics provide interpretable indicators of network connectivity and potential accessibility gaps.

### Amenity Count Map

Metric Category: _Extrinsic / Contextual Utility_

This visualization highlights the distribution of amenities across each jurisdiction using tiled spatial aggregation.

Though not a direct quality metric, this contextualizes Walkshed analysis by illustrating where amenities are dense or sparse, relative to the pedestrian network.

### Connectivity Metrics

Connectivity metrics help evaluate how navigable and efficient a pedestrian network is. Based on network measures and nomenclature: nodes = intersections, curb ramps, POIs; edges = sidewalks, crossings, footways.

These metrics answer:

- Can a person travel efficiently through the network?
- Where are the most critical or most isolated paths?
- Which areas are well-connected or fragmented?

Importantly, this section also serves as a diagnostic tool for the quality of the sidewalk graph data itself, not just a measure of real-world connectivity.

For example, extremely low degree or eigenvector centrality values in areas known to be active or dense may signal incomplete or improperly linked data, rather than true isolation.

Anomalously high betweenness centrality in segments that don't align with known mobility corridors may indicate that the map accidentally simplified the shape of the sidewalk too much or that perhaps it's missing nearby sidewalks or crossings that would normally spread out the traffic. As such, connectivity metrics offer surrogate indicators of data validity, highlighting places where the digital network may need further QA, even if the physical infrastructure is in place.

Reviewing these metrics in tandem with the spatial layout and ground-truth knowledge allows data stewards to catch errors of omission or topological misrepresentation. Please note that of these three cities, Bellevue is the most densely populated, Goldendale is the least dense, and Everett's population density is between the other two cities.

| Metric                          | Bellevue | Everett | Goldendale | What it means                                                                          |
|:--------------------------------|:---------|:--------|:-----------|:---------------------------------------------------------------------------------------|
| **IXN Quality**                 | 0.148    | 0.179   | _0.208_    | **Intersection quality**: how well intersections are connected and aligned in geometry |
| **Degree Centrality**           | 0.039    | 0.033   | _0.031_    | How many immediate connections a node has; higher = more access options                |
| **Eigenvector Centrality**      | 0.148    | 0.132   | _0.122_    | Measures influence: a node is important if it's connected to other important nodes     |
| **Node Betweenness Centrality** | 0.00013  | 0.00011 | _0.00001_  | Measures how often a node lies on the shortest path between others; shows bottlenecks  |
| **Edge Betweenness Centrality** | 0.00885  | 0.00724 | _0.0062_   | Like node betweenness, but for **paths**; high values indicate critical paths          |

For each metric, the OS-CONNECT QA/QC report has:

- A **Histogram** (frequency of values across the network)
- A **Jurisdiction Map** (spatial distribution of metric values)

Here's how to interpret each:

#### IXN Metric Category: Intrinsic / Derived Structural Quality

IXN Quality Metrics estimate the ease of traversal through intersections based on attributes such as:

- Presence of curb ramps
- Crossing distance
- Markings and visibility

#### IXN Procedure

Metrics are generated using the TDEI API for each jurisdiction and downloaded using matching Dataset IDs.

Results include a numeric intersection quality score (average per city) and spatial visualizations (map and histogram).

#### IXN Interpretation

The IXN map shows how evenly mobility is supported across the jurisdiction. A higher average score indicates better structural support for safe and accessible pedestrian movement at intersections. This is not a subjective evaluation but a computed indicator derived from physical attributes.

| IXN Score     | Meaning                                                                                  |
|---------------|:-----------------------------------------------------------------------------------------|
| 0.0           | The intersection is not traversable to pedestrians from any direction.                   |
| 0.33,0.5,0.67 | Only some approaches and exits are traversable; possible missing ramps or crossings.     |
| 1.0           | All directions at the intersection are traversable; infrastructure is in good condition. |

**How to use this section to identify data quality issues**:

Detect intersections with zero traversability that may lack required connections or have misclassified curb features.

Spot mismatches between modeled traversability and real-world expectations, which may signal mistagged or missing curb ramps or crossings.

Use histograms to identify systemic gaps, e.g., large numbers of intersections with partial or no traversability suggest systematic omissions in tagging or curb data.

Look for: Histogram clusters at low values (bad) vs. a smooth spread (better).

Compare:

Everett has a wide, fairly even distribution → indicates varied terrain, many mid-quality segments.

Bellevue shows a bimodal pattern → suggests disparities, e.g., some well-served areas and some disconnected ones.

#### IXN Details

The Intersection Traversability Metric (IXN) provides a standardized way to assess the accessibility and usability of pedestrian intersections across a network. It is specifically designed to highlight whether intersections are navigable by people and whether pedestrians can safely and reliably cross the streets.

This metric helps identify gaps in infrastructure that could impede safe or accessible crossing at intersections, and is one of the core tools used to assess compliance with Complete Streets, Vision Zero, and Americans with Disabilities Act (ADA) goals.

**What is Traversability?**

Traversability refers to whether a pedestrian can safely and effectively move across an intersection given the available infrastructure. This includes:

- Whether curb ramps exist where sidewalks meet roads
- Whether a marked crossing is provided
- Whether sidewalks are continuous leading up to and away from the crossing
- The length of the crossing distance
- The slope or grade of the ramps, if present

**How is the IXN Computed?**

The metric is computed using a set of geometric and semantic rules that operate over intersections of roads and the set of paths that connect into and out of them.

Each road intersection and the pedestrian infrastructure that projects out from the intersection is assigned a Traversability Score from 0 (completely untraversable) to 1 (fully traversable). This score is based on whether every pedestrian approach and exit from the intersection satisfies specific criteria for pedestrian safety and accessibility.

The rules are defined as follows:

- Sidewalk Availability: Is there a connected, walkable sidewalk or footway approaching the intersection from at least one direction?
- Crossing Presence: Is there a mapped, tagged crossing (e.g., `highway=crossing`) at the intersection?
- Curb Ramp Condition: If the approach involves a curb, is there a curb ramp allowing a person using a wheelchair to cross?
- Connectivity: Does the crossing connect to another usable sidewalk or footway?
- Crossing Distance: Is the crossing shorter than a threshold that would be considered unsafe (e.g., >30m)?

Each rule is evaluated and the intersection is scored using a logic tree that combines these binary conditions. The score represents the maximum proportion of feasible traversals through the intersection that meet all requirements.

### Centrality Metrics

Metric Category: _Intrinsic / Topological Measures_

This section reports on network centrality: a set of graph-based metrics that describe the importance or influence of particular nodes or edges in the pedestrian network.

Metrics include:

- Degree centrality (number of direct connections)
- Eigenvector centrality (influence within well-connected regions)
- Betweenness centrality (how often a node/edge lies on the shortest path between others)
- Standard deviation of betweenness (to assess inequality in network use)

These are calculated using a Voronoi-tiled simplification of the pedestrian graph. They do not imply preference or value judgments; they are structural properties that may inform maintenance prioritization or network resilience assessment.

#### Degree Centrality Map & Histogram

- **Purpose:** Reveals how "well connected" each node is (like a transit stop with many options).
- **High values:** Indicate areas with many paths leading in/out.
- **Compare:**
    - **Bellevue** has a slightly higher average than Everett, indicating **denser network hubs**.
    - If **Goldendale** (a smaller jurisdiction) shows **many low-degree nodes**, it may signal isolated segments or a sparser grid.

#### Eigenvector Centrality

- **Purpose:** Measures influence: is this node near other "important" nodes?
- **High eigenvector + low degree?** This means the node is near a "hub" but doesn't itself connect to many paths.
- **Compare:**
    - Bellevue's higher score may reflect **concentrated downtown paths**, while Everett's slightly lower score suggests a more **distributed grid**.

#### Betweenness Centrality (Nodes & Edges)

- **Purpose:** Measures chokepoints: paths or nodes that many routes pass through.
- **High values:** Indicate **vulnerability**: if that edge or node is removed, the network is disrupted.
- **Compare:**
    - If **Everett** has more evenly distributed low values, it means **multiple alternate routes exist**.
    - A **sharp peak** in Bellevue's histogram might mean **one area bears the burden of many trips**.

Here is a table that summarizes each centrality metric and its implications for maintenance and infrastructure resilience:

| Metric                                | Meaning                                                                                  | High Value Implications                                                   | Low Value Implications                                              | Maintenance / Resilience Insights                                                                                                                                                                              |
|---------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Degree Centrality**                 | Number of directly connected paths at a node (local connectivity).                       | Node is a _local hub_ with many connections; important for accessibility. | Node is _isolated_ or has few connections; limited local options.   | **High:** Prioritize maintenance to avoid disproportionate impact on local movement. **Low:** May signal incomplete data, disconnected sidewalks, or opportunities for infill links.                           |
| **Eigenvector Centrality**            | Measures influence within the wider network; nodes connected to other "important" nodes. | Node lies within a _key, interconnected area_ (e.g., downtown core).      | Node is peripheral, not strongly tied to major hubs.                | **High:** Maintenance critical for _network cohesion_; damage could ripple across the system. **Low:** Lower urgency; may be less disruptive if degraded, but might warrant upgrades to enhance accessibility. |
| **Betweenness Centrality**            | Frequency a node/edge lies on shortest paths; indicates chokepoints or bridges.          | Node/edge is a _critical corridor_: many routes depend on it.             | Node/edge rarely used in shortest paths; alternate routes exist.    | **High:** High-priority for _preventive maintenance_ and monitoring; failure causes major detours. **Low:** Lower priority; redundancy provides resilience.                                                    |
| **Standard Deviation of Betweenness** | Inequality of betweenness across network (distribution of flow).                         | Network use is _uneven_: few chokepoints bear most load.                  | Network use is _balanced_: traffic and routes are well-distributed. | **High:** Consider adding _redundant paths_ or alternate routes to ease pressure on chokepoints. **Low:** Indicates resilient design; maintenance can be distributed evenly.                                   |

### Routing Data

The goal of presenting the routing data is to help us visualize the quality of running Walksheds.

We do this by generating routes from all amenity pairs within 0.25 miles of each other in a jurisdiction. Then, for each pair of amenities, we generate four different types of routes:

Two are generated by running the Walksheds routing API: **normative unconstrained pedestrian Walkshed** (also referred to simply as "Pedestrian Walkshed") and **manual wheelchair Walkshed** (also known as "Wheelchair Walkshed").

The other two routes are generated through running HERE's Routing API: **Unique Car Routes** and **Unique Here API Pedestrian Routes**. Note that in certain jurisdictions, if there are no amenity pairs within 0.25 miles of each other (often due to a jurisdiction only having one amenity or no amenities at all), a message will be output that says "Routing data is unavailable for this jurisdiction, due to lack of amenities within 0.25 miles."

#### Routing Metrics Table

The routing metrics table includes various metrics generated by creating the different routes from each pair of amenities. The first entry on the table for each jurisdiction will be the number of route pairs. After that, each type of route will have a success rate (the percentage of routes generated successfully), and the average duration and distance. These metrics were chosen because they were present across all the different types of routing. For the Walkshed routes, average incline, curb ramp count, and the number of segments with steep incline will be included as well. Finally, the differences in duration and distance between each profile will be displayed at the end of this table.

#### Map of Unique and Shared Routes

The map of unique and shared routes allows us to compare the routes generated by each type of routing in each jurisdiction. It does this by first merging every single route together while keeping a note of the source of the routes to determine the uniqueness of the routes. In red, we can see the "Shared Segments" found in at least two methods of routing. On the other hand, all the unique routes are also displayed in other colors, visualizing the routes that are not found through any other method of routing.

---

Previous section: [Data Sources and OS-CONNECT QA/QC Report Structure](structure.md)

Next section: [Data Infrastructure for QA/QC Report Generation](infrastructure.md)

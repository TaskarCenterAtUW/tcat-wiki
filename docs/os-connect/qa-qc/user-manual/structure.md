---
title: Data Sources and OS-CONNECT QA/QC Report Structure
nav_order: 2
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Data Sources and OS-CONNECT QA/QC Report Structure

This document explains the structure of the OS-CONNECT "Jurisdiction Snapshot" QA/QC reports.

---

All QA/QC metrics are calculated using data available through the **Transportation Data Exchange Initiative (TDEI)** platform under the `TCAT_WSP_PG` (Washington State Proviso) project group. Each jurisdiction's data consists of:

- A **metadata JSON file**
- A **GeoJSON file for nodes**
- A **GeoJSON file for edges**

Each OS-CONNECT QA/QC report is organized into the following key sections, designed to provide both **quantitative assessments** and **visual insights** into the quality and structure of the pedestrian infrastructure dataset for the jurisdiction.

### Tag Completion Subreport

This section checks whether the required descriptive information necessary for accessibility and routing analysis (called **tags**) are present for key features in the pedestrian network (sidewalks, crossings, footways). These tags are used when determining whether a path segment is usable, accessible, and safe for different types of pedestrians.

**What's assessed:**

- Sidewalk segments: Are details like width, slope (incline), surface type, and condition available?
- Crossings: Are attributes such as the presence of curb ramps, tactile paving, crossing width, and signalization documented?
- Footways and other pedestrian paths: Are relevant characteristics included?

#### Subreport A. Completeness Summary Tables

Shows the total number of segments of each type (sidewalk, crossing, footway).
Reports how many of those are "complete"—i.e., they contain all required tags.

A completeness percentage is provided for each feature type.

#### Subreport B. Tag-Level Details

Breaks down the presence of each tag by feature type.

For example, it shows the percentage of sidewalks that have tags for: length, surface, incline, width, id, and from and to nodes. It will also show the percentage of crossings, footways, and curbs that have all applicable tags.

**How to use this section:**

Use this to assess if your jurisdiction has sufficient metadata to perform meaningful accessibility analyses. Low completeness on tags like width or incline may limit wheelchair accessibility modeling.

Without complete and accurate tags, it's not possible to uniformly or comparatively assess how accessible or navigable sidewalks or crossings are. For example, a segment without a width or incline tag can't be confidently used in wheelchair routing or equity assessments.

### Walkshed Accessibility Metrics

This section estimates how far a person can travel on the pedestrian network starting from known destinations (e.g., schools, transit stops). It compares two types of pedestrian profiles, expressing different accessibility needs:

- Unconstrained Pedestrian: Assumes no mobility limitations.
- Manual Wheelchair User: Assumes the traveler needs flat, ramped, and curb-cut-equipped paths.

**What's a walkshed?**

A walkshed is the area that can be reached within a short walking distance (typically 5 or 10 minutes) from a starting location, following real paths like sidewalks and crosswalks—not "as-the-crow-flies" distances.

**How it works:**

The tool simulates walking from selected community locations, such as libraries, grocery stores, or transit stops, and maps the areas that are reachable, characterized by mobility profiles suitable to represent:

- An unconstrained pedestrian. Typified by requiring sidewalks and having no constraints on the presence of steps, raised curbs, or high elevation in up or down-hill paths along their route.
- A manual wheelchair user. Typified by requiring sidewalks, requiring inclines to be less than 8.3% grade, requiring all curbs to be ramped, and having no steps along their route.

**What's reported:**

- The total length of sidewalk reachable in each mobility profile (in meters)
- The difference in access area between the two profiles, including the count of curbs, crossings, paths, marked curbs, and lowered curbs encountered
- Visualizations: maps showing the geographic extent of reachability (the walkshed) for each profile.

**How to use this section:**

This section helps identify where accessibility barriers exist and where disconnectivity or discontinuity in the pedestrian data exists.

For example, if the walkshed for a wheelchair user is significantly smaller than that for an unconstrained pedestrian, it may indicate that the data is missing curb ramps or steep slopes, or discontinuities in the sidewalk graph exist.

**Under the hood:**

Using a network-based simulation in the Taskar Center's Walksheds tool, a reachable walkshed map is simulated for the different typified users using publicly available points of interest (POIs) as starting points. The QA/QC reports provide these metrics:

- Length of the reachable network
- Number and types of path elements included

### Amenity Density Map

The map helps visualize areas with higher or lower service density, supporting assessments of access.

This section maps the density and spatial distribution of key services and destinations ('amenities' in this analysis include the set of amenities listed below, crafted from a list provided by King County Metro for its Connected Through Transit analyses).

**What's shown:**

- A map with amenities like parks, grocery stores, clinics, schools, and transit hubs
- How many amenities are reachable by different pedestrian profiles

**What amenities are included?**

- Community Center
- Day Care Center
- Place of Worship
- Emergency Shelter
- Food Bank
- Library
- Hospital
- Residential Treatment Center
- Work Source Site
- Federally Qualified Health Center (FQHC)
- FQHC Tribal
- College
- Shopping Center
- Apprentice Program
- WIC Clinic
- WIC Vendor
- Farmers Market
- Middle or High School
- Elementary School
- Other School
- Municipal Services
- ORCA Lift Enrollment Center
- Housing Entry Point
- Senior Center
- Grocery Store
- Election Drop Box
- Nursing Home
- Assisted Living Facility
- ORCA Ticket Vending Machine (TVM)
- ORCA Fare Outlet
- Accessibility and Disability Assistance
- Social Facility
- School
- Polling Station
- Bus Stop
- Station
- Fitness Center
- Park
- Supermarket

**How to use this section:**

Even if sidewalks are present, access is only meaningful if people can actually reach the places they need to go.

This section, in conjunction with the Walksheds section, could help identify (1) areas where data integrity might be prioritized and (2) areas where there is a lack of pedestrian data in areas with services.

### Connectivity and Network Structure Metrics

This section provides a more detailed look at the structure of the pedestrian environment by providing insight into the navigability and resilience of the pedestrian network using graph-theoretic analysis. It answers questions like:

- Are sidewalks and crossings well-connected?
- Are there areas where a single missing link creates a major barrier?
- Which intersections are most important for overall access?

Connectivity metrics offer surrogate indicators of data validity, highlighting places where the digital network may need further QA, even if the physical infrastructure is in place.

Key concepts and definitions:

- **Connectivity** refers to how well the pedestrian network is linked together. A well-connected network allows people to reach more places with fewer detours.
- **Traversability (IXN Scores):** This measures the accessibility of crossings at intersections. A high-quality intersection typically has curb ramps, short crossing distances, and signals or markings that make it safe and usable for people with disabilities.
- **Importance of Sidewalks or Crossings:** Some paths or intersections are more critical than others because they connect many parts of the network. The report includes measures that help identify these key links:
    - **Path Usage Frequency (Betweenness):** Shows which sidewalk segments are used most often in the shortest routes. These are often "critical links."
    - **Intersection Importance (Degree)**: Indicates how many sidewalk segments connect to each intersection. Higher values mean more connectivity.
    - **Resilience to Disruptions:** The report also shows whether access is evenly distributed or overly dependent on a few key segments—this can help assess how resilient the network is to construction, damage, or closures.

**How to use this section:**

This section evaluates how well the pedestrian network is connected and which parts of the network are critical for the overall structure.

These network-based metrics evaluate the **role and importance of each path or intersection** within the larger pedestrian network. These metrics can help planners and local governments focus maintenance or upgrades where they will have the greatest impact—such as repairing a crossing that connects two neighborhoods or fixing a broken curb ramp that limits access to a school.

The connectivity metrics include:

- **Traversability Scores (IXN Quality Metrics):**
  Ratings of intersection quality, considering curb ramp presence, crossing distances, and geometry.
    - OS-CONNECT report includes:
        - Scores from 0 to 1 at each intersection based on traversability rules (e.g., curb ramp presence, crossing continuity).
        - Histograms and spatial maps showing score distributions of the intersections in each dataset.
    - How to use traversability to identify data quality issues:
        - Detect intersections with zero traversability that may lack required connections or have misclassified curb features.
        - Spot mismatches between modeled traversability and real-world expectations, which may signal mistagged or missing curb ramps or crossings.
        - Use histograms to identify systemic gaps—e.g., large numbers of intersections with partial or no traversability suggest systematic omissions in tagging or curb data.
- **Degree Centrality:**
  Number of directly connected paths at a node; indicates local accessibility. Effectively counts how many other paths connect to each node in the pedestrian network.
    - OS-CONNECT report includes: Average score, histogram, and spatial distribution.
    - How to use connectivity to identify data quality issues:
        - Low degree centrality at intersections expected to be well-connected may indicate missing connecting segments.
        - Isolated clusters of high or low degree centrality could reflect inconsistent application of footway or sidewalk features or fragmentation in the graph due to topology errors, which is a flaw with the data.
- **Eigenvector Centrality:**
  Importance of nodes based on connections to other highly connected nodes. Effectively measures the importance of a node based on its connections to other well-connected nodes—similar to how well-integrated it is within the network.
    - OS-CONNECT report includes: Average score, histogram, and spatial distribution.
    - How to use eigenvector centrality to identify data quality issues:
        - A low eigenvector centrality in central areas may suggest disconnected links or misaligned node attributes that prevent propagation, which is a data issue.
        - High eigenvector spikes in otherwise sparse networks may indicate artifacts of data modeling (e.g., duplicate links or routing loops).
- **Node and Edge Betweenness Centrality:**
  Measures the extent to which nodes or edges serve as bridges across the network—critical for identifying key connectors or potential bottlenecks. Effectively measures how often a path or node lies on shortest paths between other parts of the network—indicating how critical it is to the overall structure.
    - OS-CONNECT report includes:
        - Average and standard deviation values for both nodes and edges.
        - Histograms and maps to visualize central paths.
    - How to use betweenness centrality to identify data quality issues:
        - Overconcentration of high-betweenness paths may indicate a fragile network highly dependent on a few segments, possibly due to missing parallel paths or links.
        - High betweenness on low-degree nodes may point to data modeling issues where long paths are connected through bottleneck features.
- **Standard Deviation of Betweenness:**
  Highlights network fragmentation or uneven distribution of access. Quantifies how unevenly access is distributed across the network.
    - OS-CONNECT reports: summary statistics, histograms, and maps showing variability.
    - How to use the standard deviation of betweenness centrality to identify data quality issues:
        - High standard deviation may signal under-connected or misrepresented areas of the network.
        - Local spikes in deviation might point to critical errors in segment connectivity or intersection misalignment.

Each metric is accompanied by spatial visualizations (e.g., heatmaps, Voronoi tiles) and summary statistics.

---

Previous section: [Understanding QA/QC Reporting for OS-CONNECT](index.md)

Next section: [OS-CONNECT QA/QC Report Subsections in Detail](metrics.md)

---
title: Walkshed Information & Sidewalk Score
nav_order: 9
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Walkshed Information & Sidewalk Score

This section explains how to view walkshed statistics and the Sidewalk Score feature of the Walksheds tool.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Viewing Walkshed Information

After a walkshed is generated, an action pop-up appears at the bottom of the map view. Select **Walkshed Info** to open the **Walkshed Information** panel on the left side of the screen.

![Walkshed action pop-up](../../resources/images/walksheds/user-manual/sidewalk-score/walkshed-light.png#only-light)
![Walkshed action pop-up](../../resources/images/walksheds/user-manual/sidewalk-score/walkshed-dark.png#only-dark)

---

![Walkshed Information panel](../../resources/images/walksheds/user-manual/sidewalk-score/info-light.png#only-light){ .img-right }
![Walkshed Information panel](../../resources/images/walksheds/user-manual/sidewalk-score/info-dark.png#only-dark){ .img-right }

### Walkshed Information Panel

The Walkshed Information panel displays statistics about the pedestrian network within the current walkshed. It is organized into the following sections:

#### Pedestrian Edges

Counts and percentages for the features within the walkshed:

| Statistic                    | Description                                                        |
|:-----------------------------|:-------------------------------------------------------------------|
| Number of footways           | Count of footway edges in the walkshed                             |
| Number of sidewalks          | Count of sidewalk edges in the walkshed                            |
| Number of crossings          | Total crossings (marked + unmarked)                                |
| Number of marked crossings   | Crossings with visible markings                                    |
| Number of unmarked crossings | Crossings without visible markings                                 |
| Number of ramped crossings   | Crossings with curb ramps                                          |
| Number of unramped crossings | Crossings without curb ramps                                       |
| Number of paved edges        | Edges with a paved surface                                         |
| Number of unpaved edges      | Edges without a paved surface                                      |
| Percent of marked crossings  | Proportion of crossings that are marked                            |
| Percent of ramped crossings  | Proportion of crossings that have curb ramps                       |
| Percent of paved edges       | Proportion of edges that are paved                                 |
| Total walkshed length        | Combined length of all reachable edges in the walkshed (in meters) |

#### Points Extension

Displays point feature data from an extension dataset, if one is loaded. Shows **None** when no extension dataset is selected.

#### Polygons Extension

Displays polygon feature data from an extension dataset, if one is loaded. Shows **None** when no extension dataset is selected.

---

#### Sidewalk Score

A summary metric for the walkshed's overall pedestrian accessibility. Select **Calculate** to compute it.

!!! example "This is an experimental feature which may not always be enabled and made visible."

---

Previous: [Batches](batches.md)

Return: [Walksheds User Manual](index.md)

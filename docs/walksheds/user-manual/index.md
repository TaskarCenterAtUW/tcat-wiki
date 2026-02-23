---
title: Walksheds User Manual
nav_order: 1
tags:
    - User Manual
    - External
    - User
---

<!-- @format -->

## Walksheds User Manual

This user manual explains how to use the TDEI Walksheds tool.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### About the Walkshed Tool

The [Walkshed Tool](https://walkshed.tdei.us) calculates pedestrian walkshed areas around a specified origin point. A **walkshed** is the region reachable on foot (or by mobility device) within a given travel time or cost budget, given the characteristics of the surrounding pedestrian network: sidewalks, crossings, slopes, and barriers.

Unlike a simple radius, a walkshed reflects real-world travel conditions. Two points equidistant from an origin may have very different costs to reach depending on slope, raised curbs or stairs, or whether the route requires crossing a busy street. The result is a realistic map of accessible space from your chosen origin.

A TDEI account is required to sign in. You can register for one at [https://portal.tdei.us/](https://portal.tdei.us/).

---

### Quick Start

1. **Register** at [https://portal.tdei.us/](https://portal.tdei.us/) and sign in to the Walkshed Tool at [https://walkshed.tdei.us](https://walkshed.tdei.us)
2. **Select a dataset** in the **Dataset tab** and click **Build Router**
3. **Configure preferences** in the **Walkshed tab**, or choose a profile
4. **Click on the map** to set an origin point and choose a travel budget
5. **Read the results:** reachable paths are highlighted in blue

---

![Walkshed Tool](../../resources/images/walksheds/user-manual/index/walkshed-light.png#only-light)
![Walkshed Tool](../../resources/images/walksheds/user-manual/index/walkshed-dark.png#only-dark)

---

### Table of Contents

Walksheds User Manual Table of Contents

#### [Getting Started](getting-started.md)

This section explains how to sign in, load a dataset, configure preferences, and generate your first walkshed.

#### [Interface Overview](interface.md)

This section introduces the Walkshed Tool interface, including the sidebar tabs, map controls, and action pop-up.

#### [Mobility Profiles and Preferences](preferences.md)

This section explains how to select a pre-defined mobility profile and how to customize individual routing preferences.

#### [Inspecting and Editing Features](editing.md)

This section explains how to inspect network edges on the map, edit their attributes, and review or remove changes.

#### [Scenarios](scenarios.md)

This section explains how to save walksheds as named scenarios and use them to compare results across different configurations or datasets.

#### [Sidewalk Score](sidewalk-score.md)

This section explains the Sidewalk Score feature of the Walkshed Tool.

#### [Custom Cost Function](custom-cost-function.md)

This section explains how to view and modify the Python cost function used to weight network edges.


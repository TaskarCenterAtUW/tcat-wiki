---
title: Getting Started
nav_order: 2
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Getting Started

This section explains how to sign in, load a dataset, configure preferences, and generate your first walkshed.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Accessing the Walkshed Tool

The Walkshed tool is a web application, so **no download or installation is required**. It runs directly in your browser on any device, including phone, tablet, or desktop.

1. Open your preferred web browser (e.g., Chrome, Firefox, Safari, Edge)

2. Navigate to [walkshed.tdei.us](https://walkshed.tdei.us)

![Walkshed landing page](../../resources/images/walksheds/user-manual/index/walksheds-light.png#only-light)
![Walkshed landing page](../../resources/images/walksheds/user-manual/index/walksheds-dark.png#only-dark)

!!! info "Account Required"

    A TDEI account is required to use the Walkshed tool. If you do not have one, register at [portal.tdei.us](https://portal.tdei.us/) before signing in.

    For more information, refer to the [TDEI Portal User Manual: Account Registration](../../tdei/portal/user-manual/account-registration.md) guide.

---

### Select a Dataset

Before calculating a walkshed, you must load an [OpenSidewalks](../../opensidewalks/index.md) pedestrian network. Open the **Dataset tab** (settings icon) in the left sidebar. Select a dataset that has been uploaded to the [Transportation Data Exchange Initiative](../../tdei/index.md) (TDEI). For information on finding and managing datasets in TDEI, refer to the [TDEI Datasets guide](../../tdei/portal/user-manual/datasets.md).

After selecting a dataset, click **Build Router** to begin constructing the routing graph. Depending on the size of the dataset, this may take anywhere from a few seconds to a few minutes. When the router is ready, the tool will display a button to refresh&mdash;click it to load the walkshed tool with the new dataset. This step is required each time you switch datasets.

---

### Configure Preferences

Open the **Walkshed tab** (graph icon) in the left sidebar to configure walkshed preferences. Several mobility profiles are available: "Manual wheelchair", "Powered wheelchair", and "Cane". These automatically set slope limits and obstacle avoidance to sensible defaults for each mobility type.

Note that selecting a profile locks all preferences. To adjust mobility preferences manually, select the "Custom" profile and set the controls directly (see [Mobility Profiles and Preferences](preferences.md)).

---

### Set Your Origin Point and Travel Budget

Click anywhere on the map to set the origin point, or use the address search in the **Walkshed tab** to locate a specific address. In the left sidebar, choose a maximum travel cost (in seconds of estimated travel time) that determines how far the walkshed extends. The walkshed visualization updates automatically as you move the origin or adjust a preference.

---

### Reading the Results

All paths reachable from your origin within the travel budget (sidewalks, crossings, and other paths) are highlighted in **blue** on the map. Paths that fall outside the budget or are excluded by your preferences (due to excessive slope, raised curbs, stairs, etc.) are not highlighted, creating visible gaps that reflect real barriers in the pedestrian environment.

You can use the map legend controls (top-right) to additionally toggle the display of network nodes and the convex hull boundary enclosing the walkshed area. See [Walkshed Actions](interface.md#walkshed-actions) for information on how to inspect statistics, download results, and save scenarios.

---

Previous: [Walksheds User Manual](index.md)

Next: [Interface Overview](interface.md)

---
title: Datasets
nav_order: 7
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Datasets

This section explains how to select a TDEI dataset and build the routing graph used for walkshed calculations.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Overview

The **Dataset tab** (gear icon) in the sidebar is where you choose which pedestrian network the Walkshed tool uses for routing. A dataset must be selected and the router built before you can generate any walksheds.

![Dataset tab](../../resources/images/walksheds/user-manual/datasets/datasets-tab-light.png#only-light)
![Dataset tab](../../resources/images/walksheds/user-manual/datasets/datasets-tab-dark.png#only-dark)

!!! question "Want to learn more about TDEI datasets?"

    Refer to the [TDEI Portal > User Manual > Datasets](../../tdei/portal/user-manual/datasets.md) page.

---

### Selecting a Dataset

1. Open the **Dataset tab** in the left sidebar.
2. Use the search field to filter the list of available TDEI datasets by name. This field _filters_ the list: it does not accept free-text input for dataset selection.
3. Select a dataset from the filtered list. The selected dataset is highlighted in blue.

Multiple versions of the same dataset may appear (e.g., `WSP_Goldendale_City 1.2`, `1.3`, `1.4`). Select the version you want to use.

![Filtering the dataset list](../../resources/images/walksheds/user-manual/datasets/filter-light.png#only-light)
![Filtering the dataset list](../../resources/images/walksheds/user-manual/datasets/filter-dark.png#only-dark)

---

### Extension Datasets

Below the primary dataset selector, you can optionally **select an extension TDEI dataset (overlay)**. Extension datasets add supplementary sidewalk network data on top of the primary dataset. This is useful for comparing coverage or testing additions to an existing network.

- Select **None** (the default) to use only the primary dataset.
- Select an extension dataset from the list to overlay it onto the primary dataset.

The extension dataset list also has a search field for filtering. Be sure to select the intended extension dataset - the selected dataset must be highlighted in blue.

---

### Building the Router

After selecting a dataset (and optionally an extension dataset), select **Build Router** to construct the routing graph. Depending on the size of the dataset, this may take anywhere from a few seconds to a few minutes. When the router is ready, a status message will indicate that the request has been fulfilled — reload the page to load the new dataset into the tool.

!!! info

    Rebuilding the router is required each time you switch datasets or change the extension dataset selection.

    Make sure to fully **reload the page (++f5++)**  when the "Request fulfilled, reload the page" notification appears!

---

### Refreshing the Dataset List

Select the **refresh** button (circular arrow icon) next to the "Select a new TDEI dataset" label to reload the list of available datasets from the TDEI platform.

Note that this dataset list refresh button does _not_ reload the page to activate router generated from the selected datasets.

---

Previous: [Scenarios](scenarios.md)

Next: [Batches](batches.md)

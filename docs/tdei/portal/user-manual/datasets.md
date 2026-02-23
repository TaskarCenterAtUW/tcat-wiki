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

This section explains how to browse, configure, and download datasets in the TDEI Portal.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._

---

### Overview

The **Datasets** section lists datasets available within the TDEI system. It has two tabs:

| Tab                       | Description                                                                 |
|:--------------------------|:----------------------------------------------------------------------------|
| **My Project Datasets**   | Datasets belonging to your currently active project group                   |
| **All Released Datasets** | All datasets that have been publicly released across the entire TDEI system |

![Datasets — All Released Datasets tab](../../../resources/images/tdei-portal/user-manual/datasets/all-released-light.png#only-light)
![Datasets — All Released Datasets tab](../../../resources/images/tdei-portal/user-manual/datasets/all-released-dark.png#only-dark)

Each dataset entry displays:

| Field                  | Description                                                                           |
|:-----------------------|:--------------------------------------------------------------------------------------|
| **Dataset Name**       | The name of the dataset, with upload timestamp and version number                     |
| **Project Group**      | The project group the dataset belongs to                                              |
| **Service Name**       | The service the dataset is associated with                                            |
| **Type**               | The data type: `OSW`, `Flex`, or `Pathways`                                           |
| **Id**                 | The unique dataset ID; select the copy icon to copy it to your clipboard              |
| **Derived Dataset Id** | The ID of the dataset from which this one is derived; select the copy icon to copy it |
| **Action** (⋮)         | Opens the action menu for the dataset (refer to [Action](#action))                    |

---

### Filtering Datasets

Use the **Type** dropdown to quickly filter the list by dataset type (`All`, `OSW`, `Flex`, or `Pathways`).

For more specific filtering, select the **Filter** button to expand the filter panel:

| Filter            | Description                                 |
|:------------------|:--------------------------------------------|
| **Dataset**       | Search by dataset name                      |
| **Project Group** | Filter by project group name                |
| **Service**       | Filter by service name                      |
| **Dataset ID**    | Search by a specific dataset ID             |
| **Valid From**    | Filter to datasets valid from a given date  |
| **Valid To**      | Filter to datasets valid up to a given date |

![Datasets filter panel](../../../resources/images/tdei-portal/how-to/download-os-connect/filter-light.png#only-light)
![Datasets filter panel](../../../resources/images/tdei-portal/how-to/download-os-connect/filter-dark.png#only-dark)

Select **Clear** next to any field to reset that filter, or use **Sort by** to change the sort order. Select the **Refresh (↻)** button to refresh the list.

---

### Action

Select the **action menu** (⋮) on the right side of any dataset row to access the following actions:

| Action                 | Description                                                                                                |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------|
| **Open in Workspaces** | Opens the dataset in the [Workspaces](../../../../workspaces/index.md) editing platform                    |
| **Download Metadata**  | Downloads the metadata associated with the dataset                                                         |
| **Clone Dataset**      | Creates a copy of the dataset, allowing you to make changes without affecting the original                 |
| **Download**           | Downloads the dataset files in a chosen format (see [Downloading a Dataset](#downloading-a-dataset) below) |

![Datasets action menu](../../../resources/images/tdei-portal/user-manual/datasets/action-light.png#only-light)
![Datasets action menu](../../../resources/images/tdei-portal/user-manual/datasets/action-dark.png#only-dark)

---

### Downloading a Dataset

1. Locate the dataset you want to download in the list

2. Select the **action menu** (⋮) on the right side of the dataset row

3. Select **Download** from the menu

4. In the download dialog, use the **Select Format** dropdown to choose your preferred file format, then select **Download**

![Download dialog format selection](../../../resources/images/tdei-portal/user-manual/datasets/format-light.png#only-light)
![Download dialog format selection](../../../resources/images/tdei-portal/user-manual/datasets/format-dark.png#only-dark)

!!! info "Looking for OS-CONNECT datasets?"

    For a step-by-step walkthrough of downloading [OS-CONNECT](../../../../os-connect/index.md) datasets specifically, refer to the [How To: Download OS-CONNECT Data from the TDEI Portal](../how-to/download-os-connect.md) guide.

---

Previous: [Services](services.md)

Next: [Feedback](feedback.md)

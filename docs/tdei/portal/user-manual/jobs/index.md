---
title: Jobs
nav_order: 9
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Jobs

This section explains how to create and monitor processing jobs in the TDEI Portal.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._

---

### Overview

The **Jobs** section lists all processing jobs you have access to within the TDEI system. Jobs allow users to submit requests for data processing operations such as validation, format conversion, quality metric calculation, and more.

![Jobs page](../../../../resources/images/tdei-portal/user-manual/jobs/jobs-light.png#only-light)
![Jobs page](../../../../resources/images/tdei-portal/user-manual/jobs/jobs-dark.png#only-dark)

Each job entry displays:

| Column           | Description                                                                                                                   |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------|
| **Job Type**     | The type of processing operation                                                                                              |
| **Job Id**       | A unique numeric identifier; select it to view full job details                                                               |
| **Submitted By** | The email address of the user who submitted the job                                                                           |
| **Message**      | A summary of the job inputs; select **Show more** to expand, or **Download Result** to retrieve the output of a completed job |
| **Created On**   | The date and time the job was submitted                                                                                       |
| **Status**       | The current status of the job (e.g., Completed, Failed, In-Progress, Abandoned) and its duration                              |

---

### Filtering Jobs

The filter bar at the top of the Jobs page provides the following controls:

| Control           | Options                                                                                                                                                                                                                                            |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Search Job Id** | Search by numeric job ID                                                                                                                                                                                                                           |
| **Job Type**      | All, Clone Dataset, Confidence - Calculate, Filter Dataset by BBox, Dataset Incline Tag, Dataset Publish, Dataset Reformat, Dataset Road Tag, Dataset Spatial Join, Dataset Union, Dataset Upload, Dataset Validate, Edit Metadata, Quality Metric |
| **Status**        | All, Completed, Failed, In-Progress, Abandoned                                                                                                                                                                                                     |
| **Show**          | All, Submitted by me                                                                                                                                                                                                                               |

Select **Refresh (↻)** to refresh the job list.

---

### Creating a Job

Select the **Create Job** button (top right) to open the **Create New Job** page.

![Create New Job page](../../../../resources/images/tdei-portal/user-manual/jobs/create-light.png#only-light)
![Create New Job page](../../../../resources/images/tdei-portal/user-manual/jobs/create-dark.png#only-dark)

Select a **Job Type** from the dropdown. Once selected, the relevant input fields for that job type will appear. Fill in the required inputs and select **Create** to submit the job. Select **Cancel** to return to the Jobs list without submitting.

Once submitted, the job will appear in the Jobs list and can be tracked by its Job Id and Status.

---

### Job Types

The following job types are available in the **Create New Job** form. Select a job type below for details on its inputs.

| Job Type                                                            | Description                                                  |
|:--------------------------------------------------------------------|:-------------------------------------------------------------|
| [OSW - Validate](osw-validate.md)                                   | Validate an OSW dataset                                      |
| [Flex - Validate](flex-validate.md)                                 | Validate a GTFS-Flex dataset                                 |
| [Pathways - Validate](pathways-validate.md)                         | Validate a GTFS-Pathways dataset                             |
| [OSW - Convert](osw-convert.md)                                     | Convert an OSW dataset between OSW and OSM formats           |
| [Confidence Calculation](confidence-calculation.md)                 | Calculate confidence scores for a dataset                    |
| [Quality Metric IXN Calculation](quality-metric-ixn-calculation.md) | Calculate intersection quality metrics for a dataset         |
| [Filter Dataset By BBox](filter-dataset-by-bbox.md)                 | Extract a subgraph of a dataset within a bounding box        |
| [Dataset Tag Road](dataset-tag-road.md)                             | Associate sidewalks with the road network based on proximity |
| [Quality Metric Tag](quality-metric-tag.md)                         | Calculate quality metrics on dataset element tags            |
| [Spatial Join](spatial-join.md)                                     | Perform a spatial join between two datasets                  |
| [Dataset Union](dataset-union.md)                                   | Merge spatial data from two datasets into one                |

---

Previous: [Feedback](../feedback.md)

Return: [TDEI Portal User Manual](../index.md)

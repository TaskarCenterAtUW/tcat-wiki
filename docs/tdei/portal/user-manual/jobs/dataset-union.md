---
title: Dataset Union
nav_order: 11
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Dataset Union

This page explains how to use the Dataset Union job to merge spatial data from two datasets.

---

### Function

Merges spatial data from two datasets by unifying overlapping nodes, edges, and polygons into consolidated geometries. It identifies equivalent nodes based on proximity, aligns and merges overlapping edges, and combines adjacent polygons, producing a single cohesive output dataset.

---

### Job Creation Form

![Dataset Union form](../../../../resources/images/tdei-portal/user-manual/jobs/dataset-union-light.png#only-light)
![Dataset Union form](../../../../resources/images/tdei-portal/user-manual/jobs/dataset-union-dark.png#only-dark)

<div class="full-width" markdown>

| Field                 | Required | Description                                                                            |
|:----------------------|:---------|:---------------------------------------------------------------------------------------|
| **First Dataset Id**  | Yes      | Dataset id defined to be unioned                                                       |
| **Second Dataset Id** | Yes      | Dataset id defined to be unioned                                                       |
| **Proximity**         | No       | Proximity value to identify equivalent nodes in meters. Default value is `0.5` meters. |

</div>

??? quote "Full job description"

    _This function merges spatial data from two datasets by unifying overlapping nodes, edges, and polygons into consolidated geometries._

    _It identifies equivalent nodes based on proximity, aligns and merges overlapping edges, and combines adjacent polygons._

    _The function outputs a single cohesive dataset._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

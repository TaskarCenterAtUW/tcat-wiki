---
title: Dataset Tag Road
nav_order: 8
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Dataset Tag Road

This page explains how to use the Dataset Tag Road job to associate sidewalks with a nearby road network.

---

### Function

Associates sidewalks from a target dataset with the road network from a source dataset based on proximity. Specifically, any part of the road network that is within a 5-meter buffer zone around the sidewalks in the target dataset gets tagged accordingly. This ensures that sidewalks are accurately mapped in relation to nearby roads, facilitating better data integration and analysis between different geographic datasets.

---

### Job Creation Form

![Dataset Tag Road form](../../../../resources/images/tdei-portal/user-manual/jobs/dataset-tag-road-light.png#only-light)
![Dataset Tag Road form](../../../../resources/images/tdei-portal/user-manual/jobs/dataset-tag-road-dark.png#only-dark)

<div class="full-width" markdown>

| Field                 | Required | Description                                         |
|:----------------------|:---------|:----------------------------------------------------|
| **Source Dataset Id** | Yes      | Dataset from which the road network to be retrieved |
| **Target Dataset Id** | Yes      | Dataset for which the road network is to be tagged  |

</div>

??? quote "Full job description"

    _This process involves associating sidewalks from a target dataset with the road network from a source dataset based on proximity._

    _Specifically, any part of the road network that is within a 5-meter buffer zone around the sidewalks in the target dataset gets tagged accordingly._

    _This method ensures that sidewalks are accurately mapped in relation to nearby roads, facilitating better data integration and analysis between different geographic datasets._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

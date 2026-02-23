---
title: Filter Dataset By BBox
nav_order: 7
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Filter Dataset By BBox

This page explains how to use the Filter Dataset By BBox job to extract a subgraph of a dataset within a bounding box.

---

### Function

Returns a subgraph of a dataset that falls within a specified bounding box, defined by west (longitude), south (latitude), east (longitude), and north (latitude) coordinates.

---

### Job Creation Form

![Filter Dataset By BBox form](../../../../resources/images/tdei-portal/user-manual/jobs/filter-dataset-by-bbox-light.png#only-light)
![Filter Dataset By BBox form](../../../../resources/images/tdei-portal/user-manual/jobs/filter-dataset-by-bbox-dark.png#only-dark)

<div class="full-width" markdown>

| Field               | Required | Description                                          | Format / Options |
|:--------------------|:---------|:-----------------------------------------------------|:-----------------|
| **TDEI Dataset Id** | Yes      | Dataset ID to which the bounding box will be applied | —                |
| **File Type**       | Yes      | Dataset output file type                             | `OSM` or `OSW`   |

</div>

**Bounding Box Value** (required):

<div class="full-width" markdown>

| Coordinate | Description                 | Format          |
|:-----------|:----------------------------|:----------------|
| **West**   | West coordinate (longitude) | Decimal degrees |
| **South**  | South coordinate (latitude) | Decimal degrees |
| **East**   | East coordinate (longitude) | Decimal degrees |
| **North**  | North coordinate (latitude) | Decimal degrees |

</div>

!!! info

    A bounding box defines the search area by specifying the latitude and longitude coordinates of its corners. These coordinates should be provided as a string in the order: west (longitude), south (latitude), east (longitude), north (latitude). This format outlines the geographical area to be searched within the defined perimeter.

??? quote "Full job description"

    _When provided with a tdei_dataset_id, this request returns a subgraph dataset that falls within a specified bounding box defined by the coordinates (xmin, ymin, ymax, xmax)._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

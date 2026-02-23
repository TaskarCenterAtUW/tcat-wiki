---
title: Quality Metric IXN Calculation
nav_order: 6
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Quality Metric IXN Calculation

This page explains how to use the Quality Metric IXN Calculation job to calculate intersection quality metrics for a dataset.

---

### Function

Calculates the intersection quality metric for a dataset. An optional intersection polygon GeoJSON file can be provided; if not given, Voronoi polygons are generated based on the dataset area. Providing an intersection polygon file is recommended for better performance.

---

### Job Creation Form

![Quality Metric IXN Calculation form](../../../../resources/images/tdei-portal/user-manual/jobs/quality-metric-ixn-calculation-light.png#only-light)
![Quality Metric IXN Calculation form](../../../../resources/images/tdei-portal/user-manual/jobs/quality-metric-ixn-calculation-dark.png#only-dark)

<div class="full-width" markdown>

| Field                   | Required | Description                                                                                        | Format     |
|:------------------------|:---------|:---------------------------------------------------------------------------------------------------|:-----------|
| **TDEI Dataset Id**     | Yes      | Dataset id of the dataset for which Intersection Quality metric is to be calculated                | —          |
| **Attach GeoJson file** | No       | _(Optional)_ GeoJSON intersection polygon file to be used to calculate intersection quality metric | `.geojson` |

</div>

??? quote "Full job description"

    _Initiates the Intersection Quality calculation for requested `tdei_dataset_id` with optional intersection polygon file._

    _Intersection polygon file can be a GeoJSON file containing one or more polygons._

    _If intersection polygon file is not given the system creates Voronoi polygons based on the dataset area._

    _It is recommended to add intersection polygon file for better performance._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

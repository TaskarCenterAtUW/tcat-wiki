---
title: Confidence Calculation
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Confidence Calculation

This page explains how to use the Confidence Calculation job to calculate confidence scores for a dataset.

---

### Function

Calculates the confidence score for a dataset. An optional sub-regions GeoJSON file can be provided; if given, confidence scores are calculated for each polygon in the sub-regions file.

---

### Job Creation Form

![Confidence Calculation form](../../../../resources/images/tdei-portal/user-manual/jobs/confidence-calculation-light.png#only-light)
![Confidence Calculation form](../../../../resources/images/tdei-portal/user-manual/jobs/confidence-calculation-dark.png#only-dark)

<div class="full-width" markdown>

| Field                     | Required | Description                                                        | Format     |
|:--------------------------|:---------|:-------------------------------------------------------------------|:-----------|
| **TDEI Dataset Id**       | Yes      | Dataset id of the dataset for which confidence is to be calculated | —          |
| **Attach Subregion File** | No       | Sub regions GeoJSON file for which confidence to be calculated     | `.geojson` |

</div>

??? quote "Full job description"

    _Initiates the confidence calculation for requested tdei_dataset_id with optional sub-regions._

    _Sub-regions file is a GeoJSON file containing one or more polygons._

    _If the sub-region file is given as an input, the confidence score of each polygon inside the sub-region file will be calculated._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

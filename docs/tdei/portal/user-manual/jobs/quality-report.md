---
title: Quality Report
nav_order: 12
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Quality Report

This page explains how to use the Quality Report job to generate a quality report for a dataset.

---

### Function

Invoked quality report generation for the specified `tdei_dataset_id`.

---

### Job Creation Form

![Quality Report form](../../../../resources/images/tdei/portal/user-manual/jobs/12-quality-report-light.avif#only-light)
![Quality Report form](../../../../resources/images/tdei/portal/user-manual/jobs/12-quality-report-dark.avif#only-dark)

<div class="full-width" markdown>

| Field               | Required | Description                                          |
| :------------------ | :------- | :--------------------------------------------------- |
| **TDEI Dataset Id** | Yes      | ID of dataset for which the report will be generated |

</div>

??? quote "Full job description"

    _Initiates the Quality report generation for requested `tdei_dataset_id`._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

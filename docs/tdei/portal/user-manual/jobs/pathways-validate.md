---
title: Pathways - Validate
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Pathways - Validate

This page explains how to use the Pathways - Validate job to validate a GTFS-Pathways dataset.

---

### Function

Validates a GTFS-Pathways dataset to check the correctness of data.

---

### Job Creation Form

![Pathways - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/pathways-validate-light.png#only-light)
![Pathways - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/pathways-validate-dark.png#only-dark)

<div class="full-width" markdown>

| Field                | Required | Description                       | Format |
|:---------------------|:---------|:----------------------------------|:-------|
| **Attach data file** | Yes      | GTFS-Pathways dataset to validate | `.zip` |

</div>

??? quote "Full job description"

    _Allows a user to validate GTFS Pathways dataset to check the correctness of data._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

---
title: Flex - Validate
nav_order: 2
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Flex - Validate

This page explains how to use the Flex - Validate job to validate a GTFS-Flex dataset.

---

### Function

Validates a GTFS-Flex dataset to check the correctness of data.

---

### Job Creation Form

![Flex - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/flex-validate-light.png#only-light)
![Flex - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/flex-validate-dark.png#only-dark)

<div class="full-width" markdown>

| Field                | Required | Description                   | Format |
|:---------------------|:---------|:------------------------------|:-------|
| **Attach data file** | Yes      | GTFS-Flex dataset to validate | `.zip` |

</div>

??? quote "Full job description"

    _Allows a user to validate GTFS Flex dataset to check the correctness of data._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

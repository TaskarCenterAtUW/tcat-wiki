---
title: OSW - Validate
nav_order: 1
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## OSW - Validate

This page explains how to use the OSW - Validate job to validate an OSW dataset.

---

### Function

Validates an OSW dataset to check the correctness of data.

---

### Job Creation Form

![OSW - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/osw-validate-light.png#only-light)
![OSW - Validate form](../../../../resources/images/tdei-portal/user-manual/jobs/osw-validate-dark.png#only-dark)

<div class="full-width" markdown>

| Field                | Required | Description             | Format |
|:---------------------|:---------|:------------------------|:-------|
| **Attach data file** | Yes      | OSW dataset to validate | `.zip` |

</div>

??? quote "Full job description"

    _Allows a user to validate osw dataset to check the correctness of data._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

---
title: OSW - Sanitize
nav_order: 2
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## OSW - Sanitize

This page explains how to use the OSW - Sanitize job to sanitize an OSW dataset.

---

### Function

Sanitizes an OSW dataset to remove invalid or unsupported values.

---

### Job Creation Form

![OSW - Sanitize form](../../../../resources/images/tdei/portal/user-manual/jobs/02-osw-sanitize-light.avif#only-light)
![OSW - Sanitize form](../../../../resources/images/tdei/portal/user-manual/jobs/02-osw-sanitize-dark.avif#only-dark)

<div class="full-width" markdown>

| Field                | Required | Description             | Format |
| :------------------- | :------- | :---------------------- | :----- |
| **Attach data file** | Yes      | OSW dataset to sanitize | `.zip` |

</div>

??? quote "Full job description"

    _Allows a user to sanitize an OSW dataset by correcting invalid or unsupported values.

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

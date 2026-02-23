---
title: OSW - Convert
nav_order: 4
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## OSW - Convert

This page explains how to use the OSW - Convert job to convert an OSW dataset to OSM format, or vice versa.

---

### Function

Converts an OSW dataset to OSM format, or vice versa.

---

### Job Creation Form

![OSW - Convert form](../../../../resources/images/tdei-portal/user-manual/jobs/osw-convert-light.png#only-light)
![OSW - Convert form](../../../../resources/images/tdei-portal/user-manual/jobs/osw-convert-dark.png#only-dark)

<div class="full-width" markdown>

| Field                | Required | Description              | Format / Options                                                                        |
|:---------------------|:---------|:-------------------------|:----------------------------------------------------------------------------------------|
| **Source Format**    | Yes      | Format of the input file | `OSW` or `OSM`                                                                          |
| **Target Format**    | Yes      | Desired output format    | `OSW` or `OSM`                                                                          |
| **Attach data file** | Yes      | Dataset file to convert  | Source Format = OSM:<br>`.pbf`, `.osm`, or `.xml`<br><br>Source Format = OSW:<br>`.zip` |

</div>

!!! info

    The allowed upload format changes depending on the selected **Source Format**.

??? quote "Full job description"

    _This request facilitates the conversion of an OSW dataset to OSM format, or vice versa._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

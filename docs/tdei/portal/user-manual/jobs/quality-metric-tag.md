---
title: Quality Metric Tag
nav_order: 9
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Quality Metric Tag

This page explains how to use the Quality Metric Tag job to calculate quality metrics on dataset element tags.

---

### Function

Calculates quality metrics on dataset element tags. Tags are the specific attributes or characteristics relevant to the OSW data entity. For example, entities like Footway, Crossing, and Sidewalk have tags such as `surface`, `width`, `incline`, and `length`, indicating attributes like the material, size, slope, and distance.

---

### Job Creation Form

![Quality Metric Tag form](../../../../resources/images/tdei-portal/user-manual/jobs/quality-metric-tag-light.png#only-light)
![Quality Metric Tag form](../../../../resources/images/tdei-portal/user-manual/jobs/quality-metric-tag-dark.png#only-dark)

<div class="full-width" markdown>

| Field               | Required | Description                                                    | Format  |
|:--------------------|:---------|:---------------------------------------------------------------|:--------|
| **TDEI Dataset Id** | Yes      | Dataset ID for calculating the quality metrics of element tags | —       |
| **Attach File**     | Yes      | OSW dataset element tag list                                   | `.json` |

</div>

!!! info

    Example file format: [tag-quality.json](https://raw.githubusercontent.com/TaskarCenterAtUW/TDEI-osw-datasvc-ts/dev/schema/tag-quality.json). OSW tag schema definition: [osw-tag-definition.json](https://github.com/OpenSidewalks/OpenSidewalks-Schema/blob/Audiom/opensidewalks.schema.json#L5).

??? quote "Full job description"

    _Calculates the quality metric on a dataset element tags for requested tdei_dataset_id._

    _Tags are the specific attributes or characteristics relevant to the OSW data entity._

    _For example entities like Footway, Crossing, and Sidewalk have tags such as surface, width, incline, and length, indicating attributes like the material, size, slope, and distance._

    _Returns the tag quality metric for the dataset element tags._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

_Return to [Jobs](index.md)._

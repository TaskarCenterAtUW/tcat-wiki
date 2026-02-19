---
title: Feedback
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Feedback

This section explains how to report data issues in the OS-CONNECT Data Viewer using the Inspect and Report Issue features.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._

---

### Inspecting a Location

You can right-click anywhere on the map at any zoom level to open an **Inspect** popup. This places a red marker at the selected location and displays:

- **Latitude** and **Longitude** of the marker
- A **Report Issue** button

![Inspect popup showing coordinates and Report Issue button](../../../resources/images/os-connect/data-viewer/user-manual/feedback/inspect.png){ width="826" }

---

### Reporting Issues

If you notice a data issue — such as a missing sidewalk, incorrect curb type, or significantly misaligned feature — you can report it directly from the Data Viewer.

#### How to Report an Issue

1. **Right-click** anywhere on the map (at any zoom level) to open the inspect popup
2. A red marker appears at the selected location, showing the latitude and longitude
3. Select the **Report Issue** button
4. The **Report Issue** form opens with the following fields:

| Field                   | Description                                                | Required |
|:------------------------|:-----------------------------------------------------------|:---------|
| **Latitude, Longitude** | The coordinates of the marker (greyed out, non-adjustable) | Auto     |
| **Issue Description**   | A text field to describe the data issue                    | Yes      |
| **Email ID**            | Your email address, for any follow-up                      | Yes      |
| **Name**                | Your name (optional)                                       | No       |

5. Fill in the required fields and select **Submit Issue** (or select **Close** to cancel)

![Report Issue form](../../../resources/images/os-connect/data-viewer/user-manual/feedback/report.png){ width="826" }

!!! note

    The coordinates are captured automatically from the marker location and cannot be edited. Focus your description on what is wrong or missing at that location.

!!! tip "Writing Effective Reports"

    Be specific and concise in your description. Good examples:

    - _"A newly built sidewalk along the west side of this road is missing"_
    - _"This crossing is labeled as unmarked, but it actually has zebra markings"_
    - _"There is a raised curb here that is not shown in the data"_

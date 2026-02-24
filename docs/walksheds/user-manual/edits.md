---
title: Inspecting and Editing Features
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Inspecting and Editing Features

This section explains how to inspect network edges on the map, edit their attributes, and review or remove changes.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Inspecting an Edge

Click on any edge or point feature on the map to select it. The action pop-up at the bottom of the screen will display the feature's attributes and three action buttons:

![Inspect feature](../../resources/images/walksheds/user-manual/edits/inspect-light.png#only-light){ .img-right-lg }
![Inspect feature](../../resources/images/walksheds/user-manual/edits/inspect-dark.png#only-dark){ .img-right-lg }

- **Walkshed From Here:** Sets the clicked feature's location as the walkshed origin and triggers a new walkshed calculation.
- **Walkshed To Here:** Calculates a walkshed that includes this feature as a destination point.
- **Edit Feature** (pencil icon): Opens the attribute editor for this feature (see below).

---

### Editing Edge Attributes

After selecting a network feature, click **Edit Feature** (pencil icon) in the action pop-up to modify its attributes. After saving your changes, the tool will automatically recalculate the walkshed using the updated attributes.

This ability provides a way to correct an error in the source data or to "try out" a potential infrastructure improvement. For example, you might mark an inaccessible crossing as having curb ramps to observe the effect on the walkshed while planning new construction.

![Feature editor](../../resources/images/walksheds/user-manual/edits/edit-light.png#only-light)
![Feature editor](../../resources/images/walksheds/user-manual/edits/edit-dark.png#only-dark)

---

### Reviewing and Removing Changes

The **Edits tab** (pencil icon) in the left sidebar lists any attribute edits. From there you can review the specific attributes that were modified for each feature and remove edits to restore the original data values.

![Edits tab](../../resources/images/walksheds/user-manual/edits/tab-light.png#only-light)
![Edits tab](../../resources/images/walksheds/user-manual/edits/tab-dark.png#only-dark)

---

Previous: [Mobility Profiles and Preferences](preferences.md)

Next: [Scenarios](scenarios.md)

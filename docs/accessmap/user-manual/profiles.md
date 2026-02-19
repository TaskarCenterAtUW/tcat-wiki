---
title: Mobility Profiles and Preferences
nav_order: 4
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Mobility Profiles and Preferences

This section explains how to select a pre-defined mobility profile and how to customize individual routing preferences.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Profile Selection

AccessMap includes several pre-defined **mobility profiles**, each designed to optimize routing for a specific set of needs. Profiles set recommended default values for routing preferences such as maximum steepness and barrier avoidance.

The profile panel is located in the [sidebar](interface.md#sidebar). Select a profile to apply it to your route planning.

![Profile selection panel](../../resources/images/accessmap/user-manual/profiles/profiles-light.png#only-light)
![Profile selection panel](../../resources/images/accessmap/user-manual/profiles/profiles-dark.png#only-dark)

| Profile                | Description                                                                                                                        |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| **Manual wheelchair**  | Optimized for manual wheelchair users — avoids steep inclines, raised curbs, and inaccessible crossings                            |
| **Powered wheelchair** | Optimized for powered wheelchair users — allows somewhat steeper inclines than the manual wheelchair profile                       |
| **Support cane**       | Optimized for users who use a cane or walking aid — higher slope tolerance and permits raised curbs and stairs                     |
| **BLV profile**        | Optimized for blind and low-vision users — no steepness restrictions and enables all screen reader alerts                          |
| **Custom**             | Allows full manual control over all individual routing preferences (see [Customizing Preferences](#customizing-preferences) below) |

!!! tip

    If you are unsure which profile to choose, start with the one that most closely matches your primary mobility consideration. You can always switch profiles or switch to **Custom** to fine-tune individual settings.

---

![Custom preferences panel](../../resources/images/accessmap/user-manual/profiles/custom-light.png#only-light){ .img-right }
![Custom preferences panel](../../resources/images/accessmap/user-manual/profiles/custom-dark.png#only-dark){ .img-right }

### Customizing Preferences

Selecting the **Custom** profile unlocks individual preference controls. These let you configure exactly how AccessMap plans your route.

#### Routing Preferences

| Preference                     | Description                                                                                                                                         |
|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Maximum uphill steepness**   | The steepest uphill incline (as a percentage) AccessMap will include in a route. Lower values produce flatter routes.                               |
| **Maximum downhill steepness** | The steepest downhill incline (as a percentage) AccessMap will include in a route. Lower values produce flatter routes.                             |
| **Street avoidance factor**    | Controls how strongly AccessMap avoids routing on streets without sidewalks. A value of `1` avoids streets; `0` treats streets like any other path. |
| **Avoid barriers**             | When enabled, AccessMap avoids paths with raised curbs and stairs that may be impassable for some users.                                            |
| **Avoid noise**                | When enabled, AccessMap avoids sidewalks and crossings adjacent to high-traffic primary streets.                                                    |

!!! abstract "Steepness Values Reference"

    Incline is expressed as a percentage grade. For reference:

    - **5%** is a gentle slope, generally manageable for most manual wheelchair users
    - **8%** is near the maximum slope permitted by ADA standards for ramps
    - **15%** is a steep hill, the default maximum in AccessMap

#### Screen Reader and Landmark Settings

These settings are particularly relevant for blind and low-vision users using a screen reader:

| Setting                | Description                                                                                                           |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------|
| **Landmarks Distance** | The maximum distance (in meters) from the route within which nearby landmarks are included in step-by-step directions |
| **Surface alerts**     | Alerts when the surface type changes along the route (e.g., from concrete to gravel)                                  |
| **Incline alerts**     | Alerts when the route transitions to a notably uphill or downhill section                                             |
| **Building alerts**    | Alerts when the route passes notable buildings                                                                        |
| **Landmark alerts**    | Alerts when the route passes nearby landmarks (benches, bins, signals, etc.) within the configured landmark distance  |

!!! tip

    Screen reader alerts are delivered through your device's assistive technology as you travel. Enable your screen reader before starting navigation so alerts are announced automatically.

---

Previous: [Interface Overview](interface.md)

Next: [Planning a Route](route-planning.md)

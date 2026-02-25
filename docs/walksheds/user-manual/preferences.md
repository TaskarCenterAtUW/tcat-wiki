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

The Walksheds tool includes several pre-defined **mobility profiles**, each designed to configure routing for a specific set of mobility needs. Profiles set recommended default values for preferences such as maximum steepness and obstacle avoidance.

Open the **Walkshed Preferences tab** in the left sidebar and select a profile to apply it.

| Profile                | Description                                                                                                                        |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| **Manual wheelchair**  | Optimized for manual wheelchair users — conservative slope limits and raised curb and stair avoidance enabled                      |
| **Powered wheelchair** | Optimized for powered wheelchair users — similar obstacle avoidance to the Manual wheelchair profile, with a higher base speed     |
| **Cane**               | Optimized for users who rely on a cane or walking aid — moderate slope limits with raised curb and stair avoidance enabled         |
| **Custom**             | Allows full manual control over all individual routing preferences (see [Customizing Preferences](#customizing-preferences) below) |

![Mobility profiles](../../resources/images/walksheds/user-manual/preferences/profiles-light.png#only-light)
![Mobility profiles](../../resources/images/walksheds/user-manual/preferences/profiles-dark.png#only-dark)

!!! tip

    If you are unsure which profile to choose, start with the one that most closely matches your primary mobility consideration. You can always switch to **Custom** to fine-tune individual settings.

#### Travel Budget (Maximum Cost)

The **Maximum Cost** slider sets the maximum travel cost (in seconds of estimated travel time) that defines how far the walkshed extends from the origin. Only edges reachable within this budget are included in the walkshed. Increasing the budget expands the walkshed; decreasing it contracts it. The cost slider can be configured on any of the mobility profiles.

---

### Customizing Preferences

Selecting the **Custom** profile unlocks individual preference controls. These directly influence which parts of the network are included in your walkshed and at what cost.

#### Slope

| Preference                     | Description                                                                                                                 |
|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| **Maximum uphill steepness**   | The steepest uphill incline (as a percentage) included in the walkshed. Edges exceeding this grade are excluded entirely.   |
| **Maximum downhill steepness** | The steepest downhill incline (as a percentage) included in the walkshed. Edges exceeding this grade are excluded entirely. |

Slope affects not only whether an edge is included, but also the travel speed assigned to it. Shallower inclines close to the ideal walking grade are traversed faster; steeper inclines reduce speed exponentially. The default cost function exempts indoor paths from slope calculations.

#### Obstacles and Crossings

| Preference                        | Description                                                                                                           |
|:----------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| **Avoid raised curbs and stairs** | When enabled, paths with raised curbs and stairs that may be impassable for some users are excluded from the network. |

With the default cost function, crossings add a fixed 30-second time penalty to account for waiting and crossing time.

#### Street Avoidance

| Preference                  | Description                                                                                                                                                                           |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Street avoidance factor** | Controls how strongly the tool avoids routing along streets rather than dedicated pedestrian infrastructure. A value near `1` avoids streets; `0` treats streets like any other path. |

Different street classifications receive different cost multipliers at the same avoidance level. Pedestrian streets and living streets are always treated as penalty-free. Service roads receive a mild penalty; residential streets a somewhat higher one; other road types the highest.

#### Departure Time

You can specify a departure date and time. This affects edges with time-restricted access, such as indoor pathways that are only open during business hours. If no time is specified, the current time is used.

---

Previous: [Interface Overview](interface.md)

Next: [Inspecting and Editing Features](edits.md)

---
title: Navigation
nav_order: 6
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Navigation

This section explains how to follow step-by-step directions and use screen reader alerts for non-visual navigation.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

![Directions panel with step-by-step cards](../../resources/images/accessmap/user-manual/navigation/directions-light.png#only-light){ .img-right-sm }
![Directions panel with step-by-step cards](../../resources/images/accessmap/user-manual/navigation/directions-dark.png#only-dark){ .img-right-sm }

### Directions Panel

To open the Directions panel, select **Directions** from the [route summary bar](route-planning.md#route-summary) at the bottom of the map. The panel displays a scrollable list of step-by-step direction cards.

Each direction card may include:

| Element                 | Description                                   | Example                                                                 |
|:------------------------|:----------------------------------------------|:------------------------------------------------------------------------|
| **Instruction**         | A turn-by-turn direction                      | "Start by heading northeast"                                            |
| **Feature description** | The type and location of the path segment     | "Use the sidewalk. Sidewalk NW of University Street"                    |
| **Surface**             | The surface material of the segment           | Concrete, Asphalt                                                       |
| **Incline**             | A description of the slope                    | Slight uphill, Minimal downhill                                         |
| **Distance**            | The length of the segment in meters           | 108.3 meters                                                            |
| **Landmarks**           | Nearby buildings and landmarks with distances | "You will pass by an office building on your left called Rainier Tower" |
| **Share Feedback**      | Open the [Share Feedback](feedback.md) form   | "Share Feedback"                                                        |

!!! tip

    AccessMap uses consistent descriptive terms for turns, such as **slight** and **sharp**, to help distinguish different types of direction changes, which is especially useful for non-visual navigation.

---

### Using Your Location During Navigation

To follow your position on the map in real time:

1. Select the **Start route from your location** button on the map

2. Allow your browser to access your device location if prompted

3. Your position is shown on the map as you move, and directions update accordingly

!!! question

    Location not being detected? Real-time location tracking requires location permissions to be enabled. If you experience issues, check your settings and ensure location access is allowed at the system level for your browser and at the browser level for the `https://accessmap.app/` website.

4. You can also select one of the directions cards and a highlight will appear on the card and the associated segment on the map will be highlighted.

![Directions panel with a card selected and map segment highlighted](../../resources/images/accessmap/user-manual/navigation/selected-light.png#only-light)
![Directions panel with a card selected and map segment highlighted](../../resources/images/accessmap/user-manual/navigation/selected-dark.png#only-dark)

---

### Screen Reader Navigation

AccessMap includes native support for screen readers and is designed to work with your device's assistive technology. For blind and low-vision users, AccessMap provides **alerts** that are announced as you travel, so you do not need to actively check the screen for directional information.

#### Enabling Alerts

Screen reader alert types are configured in the [Custom preferences panel](profiles.md#screen-reader-and-landmark-settings). The **BLV profile** enables a set of defaults recommended for blind and low-vision users, including landmark alerts.

To receive alerts through your screen reader:

1. **Enable your device's screen reader** before beginning navigation
2. Ensure the relevant **alert types** are enabled in your preferences (see [Mobility Profiles and Preferences](profiles.md))
3. **Begin navigating** — alerts will be announced automatically as you reach the next segment along the route

#### Alert Types

| Alert Type          | When It Fires                                                                                         |
|:--------------------|:------------------------------------------------------------------------------------------------------|
| **Surface alerts**  | When the path surface changes (e.g., from asphalt to gravel or concrete)                              |
| **Incline alerts**  | When the route transitions to a notably uphill or downhill section                                    |
| **Building alerts** | When the route passes nearby buildings                                                                |
| **Landmark alerts** | When the route passes a landmark such as a bench or waste bin within the configured landmark distance |

---

![Directions card with landmarks](../../resources/images/accessmap/user-manual/navigation/landmarks-light.png#only-light){ .img-right }
![Directions card with landmarks](../../resources/images/accessmap/user-manual/navigation/landmarks-dark.png#only-dark){ .img-right }

### Landmarks

AccessMap can include **landmarks** in directions and alerts to help orient users along a route. Landmarks include objects commonly encountered by pedestrians, especially useful for white cane users, such as benches, waste bins, and building entrances.

The **Landmarks Distance** setting (in the Custom profile preferences) controls how far from the route a landmark must be to be included. See [Mobility Profiles and Preferences](profiles.md#screen-reader-and-landmark-settings) for details.

---

### Rating and Post-Trip Survey

After you close the Directions panel, AccessMap may display a **rating popup** asking "Enjoying AccessMap?" You can:

1. Select a **star rating** (1–5 stars)
2. Select **Submit** to send your rating (or **Cancel** to dismiss)

After submitting a rating, a **Thank You** popup appears with a link to a **Post Trip Survey**. The survey is part of the AccessMap Mobility Study and asks questions such as:

- How likely are you to recommend AccessMap to a friend using a similar trip profile?
- How satisfied were you with your trip experience using AccessMap?
- Did you encounter any physical barriers during your trip?
- Was the information provided by AccessMap accurate for your trip?
- Would you like to suggest or add data to improve future trips for others?
- Do you generally use either screen reader or screen magnification?

Participation in the survey is voluntary. Providing an email address is only necessary for survey compensation.

![Rating popup](../../resources/images/accessmap/user-manual/navigation/rating-light.png#only-light)
![Rating popup](../../resources/images/accessmap/user-manual/navigation/rating-dark.png#only-dark)

---

Previous: [Planning a Route](route-planning.md)

Next: [Leaving Feedback](feedback.md)

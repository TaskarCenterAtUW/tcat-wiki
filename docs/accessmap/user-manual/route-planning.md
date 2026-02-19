---
title: Planning a Route
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Planning a Route

This section explains how to set a starting point and destination, plan a route, and read the route display.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Setting Your Waypoints

A route in AccessMap consists of two waypoints: an **origin** (waypoint A) and a **destination** (waypoint B). There are several ways to set waypoints:

![Search for a location](../../resources/images/accessmap/user-manual/route-planning/search-light.png#only-light){ .img-right }
![Search for a location](../../resources/images/accessmap/user-manual/route-planning/search-dark.png#only-dark){ .img-right }

#### Using the Search Bar

1. Select the **Search address** field in the sidebar

2. Type the name or address of your starting location

3. Select the correct result from the list that appears

4. Repeat to set your destination

#### Using a Feature on the Map

You can also set waypoints by tapping or clicking on any location on the map. If an element is selected, its [details popup](interface.md#inspecting-a-feature) will open, providing the options to select **Route From Here** (to set the _origin_) or **Route To Here** (to set the _destination_).

---

### Using Your Current Location as the Origin

To use your current GPS location as the starting point for your route:

1. Select the **Start route from your location** button on the map (near the map controls at the bottom right)

2. If prompted, allow your browser and AccessMap to access your precise device location

3. AccessMap will use your current position as the route origin

!!! info "Browser Permissions"

    AccessMap requires location permission from your browser to use your current position. If you deny permission, you can still plan a route by manually typing your starting address in the search bar.

---

### Understanding the Route Display

Once a route is planned, it is displayed on the map as a colored line connecting your waypoints. The color along the route conveys information about **incline grade**:

- Colors indicate whether a given segment is flat, gently sloping, or steep
- Steeper segments are visually distinct from flat or gentle ones
- Refer to the **Map Legend** (see [Interface Overview](interface.md#map-legend)) and the [incline bar](interface.md#incline-bar) at the bottom of the screen for the specific color meanings

!!! tip

    Review the color-coded route on the map before you begin traveling to identify any steep sections you may want to plan for in advance.

---

### Route Summary

![Route info popup](../../resources/images/accessmap/user-manual/route-planning/route-info-light.png#only-light){ .img-right-lg }
![Route info popup](../../resources/images/accessmap/user-manual/route-planning/route-info-dark.png#only-dark){ .img-right-lg }

A **Route** summary bar also appears at the bottom of the map showing:

- **Total distance** (in meters)
- **Estimated time** (in minutes)

The summary bar provides two buttons:

| Button         | Description                                                                                            |
|:---------------|:-------------------------------------------------------------------------------------------------------|
| **Directions** | Opens the [Directions panel](navigation.md#directions-panel) with step-by-step navigation instructions |
| **Trip Info**  | Opens the [Trip Information panel](#trip-information) with route statistics and an elevation profile   |

---

![Trip Information panel](../../resources/images/accessmap/user-manual/route-planning/trip-info-light.png#only-light){ .img-right }
![Trip Information panel](../../resources/images/accessmap/user-manual/route-planning/trip-info-dark.png#only-dark){ .img-right }

### Trip Information

Select **Trip Info** from the route summary bar to open the Trip Information panel. This panel provides a detailed overview of the planned route:

| Section                        | Description                                                                         |
|:-------------------------------|:------------------------------------------------------------------------------------|
| **Experienced elevation gain** | A chart showing elevation (height in meters) over distance (meters) along the route |
| **Total distance**             | The total length of the route in meters                                             |
| **Estimated time**             | The estimated travel time based on your mobility profile                            |
| **Steepest uphill incline**    | The steepest uphill grade encountered on the route, as a percentage                 |
| **Steepest downhill incline**  | The steepest downhill grade encountered on the route, as a percentage               |

!!! quote "Disclaimer"

    The Trip Information panel includes a disclaimer noting that routes are for informational purposes only and that users should exercise their own judgment and follow local laws and regulations.

---

### Adjusting Your Route

If the planned route does not match your needs:

- **Change your mobility profile or preferences** — different profiles optimize for different constraints, which may produce alternative routes (see [Mobility Profiles and Preferences](profiles.md))
- **Update your waypoints** — revise your origin or destination address using the search bar

---

### Sharing a Route

AccessMap routes can be shared by simply copying the URL in your browser's address bar after planning a route. The URL encodes the current map view, selected waypoints, and routing profile, so anyone who opens the link will see the same route.

!!! example "Example"

    This link is for a route in Seattle, WA from the Space Needle to Lake Union Park:

    `https://www.accessmap.app/dir?wp=-122.3493266_47.6204716%27-122.3372692_47.627025&region=wa.seattle&lon=-122.3467038&lat=47.621326&z=14.34&sa=1&mu=0.08&md=0.1&ab=1&aps=0`

    The URL parameters encode the full route state:

    | Parameter | Value                     | Meaning                                                      |
    |:----------|:--------------------------|:-------------------------------------------------------------|
    | `wp`      | `-122.3493266_47.6204716` | Origin waypoint (Space Needle): `longitude_latitude`         |
    |           | `-122.3372692_47.627025`  | Destination waypoint (Lake Union Park): `longitude_latitude` |
    | `region`  | `wa.seattle`              | Routing region                                               |
    | `lon`     | `-122.3467038`            | Map center longitude                                         |
    | `lat`     | `47.621326`               | Map center latitude                                          |
    | `z`       | `14.34`                   | Map zoom level                                               |
    | `sa`      | `1`                       | Street avoidance factor: 1                                   |
    | `mu`      | `0.08`                    | Maximum uphill grade: 8%                                     |
    | `md`      | `0.1`                     | Maximum downhill grade: 10%                                  |
    | `ab`      | `1`                       | Avoid barriers (raised curbs and stairs): enabled            |
    | `aps`     | `0`                       | Avoid primary streets (low noise): disabled                  |

---

Previous: [Mobility Profiles and Preferences](profiles.md)

Next: [Navigation](navigation.md)

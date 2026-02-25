---
title: Custom Cost Function
nav_order: 10
tags:
    - Guide
    - External
    - Developer
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Custom Cost Function

This section explains how to view and modify the Python cost function used to weight network edges.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Overview

!!! example "This is an experimental feature which may not always be enabled and made visible."

Advanced users can directly edit the Python code that computes the travel cost for each edge in the pedestrian network. This allows for highly customized walkshed calculations beyond what the standard preference sliders support.

---

### Accessing the Editor

Open the **Cost Fn tab** in the left sidebar. The current cost function is displayed and can be modified in place.

Press the **Save** button at the bottom of the sidebar tab to apply the changes to the cost function and recalculate the walkshed.

---

### The Generator Pattern

The editor does not accept a `cost_fun` function directly. Instead, the script must define a **`cost_fun_generator`** function. The tool calls `cost_fun_generator` with the current UI preference settings as arguments, and the generator must return the actual `cost_fun(u, v, d)` function used to evaluate each edge.

```python
def cost_fun_generator(
    G,
    base_speed=1.3,
    downhill=0.1,
    uphill=0.085,
    avoidCurbs=False,
    avoidPrimaryStreet=False,
    avoidRailway=False,
    avoidBuses=False,
    avoidFlex=False,
    sidewalkScore=False,
    timestamp=None,
    streetAvoidance=1,
):
    def cost_fun(u, v, d):
        # ... evaluate edge d and return a cost or None
    return cost_fun
```

#### `cost_fun_generator` Parameters

These parameters are passed automatically by the tool based on the current UI settings when the walkshed is calculated.

| Parameter            | Type        | Description                                                                                |
|:---------------------|:------------|:-------------------------------------------------------------------------------------------|
| `G`                  | graph       | The full pedestrian network graph. Useful for advanced lookups across nodes and edges.     |
| `base_speed`         | float       | Base movement speed in m/s, set by the selected mobility profile.                          |
| `downhill`           | float       | Maximum downhill grade as a decimal (e.g., `0.1` = 10%), from the Walkshed tab.            |
| `uphill`             | float       | Maximum uphill grade as a decimal (e.g., `0.085` = 8.5%), from the Walkshed tab.           |
| `avoidCurbs`         | bool        | Whether to avoid raised curbs and stairs, from the Walkshed tab.                           |
| `avoidPrimaryStreet` | bool        | Whether to avoid primary road segments and adjacent sidewalks.                             |
| `avoidRailway`       | bool        | Whether to avoid railway edges.                                                            |
| `avoidBuses`         | bool        | Whether to avoid bus edges.                                                                |
| `avoidFlex`          | bool        | Whether to avoid flex edges.                                                               |
| `sidewalkScore`      | bool        | When `True`, calculate a **Sidewalk Score** (no road edges considered)                     |
| `timestamp`          | int \| None | Departure time as Unix epoch milliseconds, or `None` for the current time.                 |
| `streetAvoidance`    | float       | Street avoidance factor from `0` (no penalty) to `1` (prohibitive), from the Walkshed tab. |

#### Return Value (`cost_fun(u, v, d)`)

The `cost_fun_generator` function must return another function that will compute the actual costs. This function is called once for every edge in the network. It must return either:

- A **non-negative float** representing the cost (in seconds) of traversing the edge, or
- **`None`**, which signals that the edge should be completely excluded from the walkshed (infinite cost).

| Parameter | Type | Description                                  |
|:----------|:-----|:---------------------------------------------|
| `u`       | int  | The ID of the incoming node.                 |
| `v`       | int  | The ID of the outgoing node.                 |
| `d`       | dict | A dictionary of edge attributes (see below). |

---

### Key Edge Attributes (`d`)

| Key              | Type  | Description                                                                                                              |
|:-----------------|:------|:-------------------------------------------------------------------------------------------------------------------------|
| `length`         | float | Length of the edge in meters.                                                                                            |
| `highway`        | str   | OSW highway type (e.g., `"footway"`, `"residential"`, `"steps"`).                                                        |
| `incline`        | float | Grade of the edge as a decimal (e.g., `0.08` = 8% uphill).                                                               |
| `footway`        | str   | OSW footway type (e.g., `"crossing"` or `"sidewalk"`).                                                                   |
| `curbramps`      | bool  | Whether a crossing has curb ramps.                                                                                       |
| `indoor`         | str   | `"yes"` if the path is indoors.                                                                                          |
| `opening_hours`  | str   | [OSM-format](https://wiki.openstreetmap.org/wiki/Key:opening_hours/specification) opening hours string for indoor paths. |
| `street_highway` | str   | The highway type of the adjacent street, if this is a sidewalk edge.                                                     |
| `is_closed`      | int   | `1` if the edge is currently closed.                                                                                     |
| `step_count`     | int   | Number of steps on a steps edge.                                                                                         |
| `pathway_mode`   | int   | [GTFS pathway mode](https://gtfs.org/documentation/schedule/reference/#pathwaystxt) (2 = stairs, 4 = escalator).         |

---

### Default Speed and Cost Model

The default cost function calculates cost as:

```
cost = street_cost_factor × (length / speed)
```

...where `speed` is derived from a modified version of Tobler's hiking function, an empirical model relating walking speed to slope. The base walking speeds used as starting points are:

| Mode               | Base Speed |
|:-------------------|:-----------|
| Walking            | 1.3 m/s    |
| Manual wheelchair  | 0.6 m/s    |
| Powered wheelchair | 2.0 m/s    |

Steps edges use a fixed speed of 0.5 m/s regardless of incline.

---

### Example: Exclude Edges Under Construction

OpenSidewalks datasets may include custom extension attributes prefixed with `ext:`. This example excludes any edge tagged with `ext:construction=yes`:

```python
def cost_fun_generator(
    G,
    base_speed=1.3,
    downhill=0.1,
    uphill=0.085,
    avoidCurbs=False,
    avoidPrimaryStreet=False,
    avoidRailway=False,
    avoidBuses=False,
    avoidFlex=False,
    sidewalkScore=False,
    timestamp=None,
    streetAvoidance=1,
):
    def cost_fun(u, v, d):
        if d.get("ext:construction") == "yes":
            return None
        # ... rest of default logic
    return cost_fun
```

---

### Example: Customize the Penalty for Crossings

```python
def cost_fun_generator(
    G,
    base_speed=1.3,
    downhill=0.1,
    uphill=0.085,
    avoidCurbs=False,
    avoidPrimaryStreet=False,
    avoidRailway=False,
    avoidBuses=False,
    avoidFlex=False,
    sidewalkScore=False,
    timestamp=None,
    streetAvoidance=1,
):
    def cost_fun(u, v, d):
        if d.get("footway") == "crossing":
            if avoidCurbs:
                if "curbramps" in d:
                    if not d["curbramps"]:
                        return None
                else:
                    return None
            length = d["length"]
            # 60-second penalty instead of the default 30
            return (length / base_speed) + 60
        # ... rest of default logic
    return cost_fun
```

---

Previous: [Walkshed Information & Sidewalk Score](sidewalk-score.md)

Return: [Walksheds User Manual](index.md)

---
title: Spatial Join
nav_order: 10
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
# exclude-from-parent-guides-list
---

<!-- @format -->

## Spatial Join

This page explains how to use the Spatial Join job to perform a spatial join operation between two datasets.

---

### Function

Performs a spatial join operation between two datasets within the TDEI system. It involves two datasets - target and source - specifying the spatial dimension entities of each to be joined (e.g., `edge`, `node`, `zone`, `point`, `line`, `polygon`). The join operation is guided by specified conditions that define how the geometries of the two datasets interact, typically involving spatial functions like intersections. Filters can be applied to both datasets to refine the data involved in the join. Aggregate functions are also defined to associate attributes from the source to the target dataset entity. The geometry columns for data elements are referenced as `geometry_target` and `geometry_source`.

_Example: Find all light poles in a source dataset within 5 m of an edge in a target dataset, and associate the `highway` attribute from the source dataset with each edge._

---

### Job Creation Form

![Spatial Join form](../../../../resources/images/tdei/portal/user-manual/jobs/10-spatial-join-light.avif#only-light)
![Spatial Join form](../../../../resources/images/tdei/portal/user-manual/jobs/10-spatial-join-dark.avif#only-dark)

The form contains a JSON text area pre-populated with the following template:

```json
{
    "target_dataset_id": "",
    "target_dimension": "",
    "source_dataset_id": "",
    "source_dimension": "",
    "join_condition": "",
    "join_filter_target": "",
    "join_filter_source": "",
    "aggregate": []
}
```

A link labeled "_(hint: check out the sample request here)_" is available below the text area. Selecting it opens a **Sample Request Body** dialog with a copy button and an **Assignment Method** dropdown to switch between **Default** and **Exclusive** examples.

---

### Assignment Methods

The request body supports two assignment methods:

**Default** (no `assignment_method` field required):

```json
{
    "target_dataset_id": "fa8e12ea-6b0c-4d3e-8b38-5b87b268e76b",
    "target_dimension": "edge",
    "source_dataset_id": "0d661b69495d47fb838862edf699fe09",
    "source_dimension": "point",
    "join_condition": "ST_Intersects(ST_Buffer(geometry_target, 5), geometry_source)",
    "join_filter_target": "highway='footway' AND footway='sidewalk'",
    "join_filter_source": "highway='street_lamp'",
    "aggregate": ["ARRAY_AGG(highway) as lamps"]
}
```

**Exclusive** (adds `"assignment_method": "exclusive"`):

```json
{
    "target_dataset_id": "fa8e12ea-6b0c-4d3e-8b38-5b87b268e76b",
    "target_dimension": "edge",
    "source_dataset_id": "0d661b69495d47fb838862edf699fe09",
    "source_dimension": "point",
    "join_condition": "ST_Intersects(ST_Buffer(geometry_target, 5), geometry_source)",
    "join_filter_target": "highway='footway' AND footway='sidewalk'",
    "join_filter_source": "highway='street_lamp'",
    "aggregate": ["ARRAY_AGG(highway) as lamps"],
    "assignment_method": "exclusive"
}
```

??? quote "Full job description"

    _Performs a spatial join operation between two datasets within the TDEI system._

    _It involves two datasets, target and source, specifying the spatial dimension entities of each to be joined, such as edges, nodes, zones, points, lines, or polygons._

    _The join operation is guided by specified conditions that define how the geometries of the two datasets interact, typically involving spatial functions like intersections._

    _Additionally, filters can be applied to both datasets to refine the data involved in the join._

    _Aggregate functions are also defined to associate the attributes from source to target dataset entity._

    _The geometry column for data elements is specified as `geometry_target` and `geometry_source`._

    _Eg: Find all light poles in source dataset within 5 m of an edge in target dataset, and associate the attribute highway from source dataset with each edge in target dataset._

    _The response includes a `job_id` for tracking the request._

    _To check the request status, refer to the location header in the response, which provides the URL for the status API endpoint._

Select **Create** to submit the job. Select **Cancel** to return to the Jobs list.

---

### OSW Spatial Join – Guide

This section explains how to use `/api/v1/osw/spatial-join` from an API or UI perspective, with concrete OSW sidewalk and pedestrian data examples that show how to pick the right `assignment_method` (`default`, `exclusive`, `shared`) and how to structure JSON requests for common real-world scenarios like curb ramps, light poles, and intersections.

---

#### Understanding the spatial-join Job Input

- **Target dataset** (`target_dataset_id`, `target_dimension`):  
  OSW dataset whose features you want to enrich (e.g., sidewalk edges or nodes).
- **Source dataset** (`source_dataset_id`, `source_dimension`):  
  OSW dataset that provides attributes (e.g., curb ramps, lighting, crossings, entrances).
- **Join condition** (`join_condition`):  
  Spatial condition using `geometry_target` and `geometry_source` (e.g., within 5 m, intersects).
- **Filters** (`join_filter_target`, `join_filter_source`):  
  Attribute filters on each side to narrow which features participate.
- **Aggregates** (`aggregate`):  
  How attributes from the source are collected and attached to each target feature.
- **Assignment method** (`assignment_method`):  
  How to resolve multiple matches between targets and sources.

---

#### What is `assignment_method`?

```json
"assignment_method": "default" | "exclusive" | "shared"
```

- **`default`**: **many-to-many** – each target keeps **all** matching source features.
- **`exclusive`**: **one-to-one** – each target gets at most one source, and each source is assigned to at most one target (competitive closest assignment).
- **`shared`**: **one-to-many** – each target gets its best (closest) source, but a source may be shared by many targets.

Choose the method based on the **real-world relationship** between the two datasets, not just what is technically possible.

---

#### When to use which method

##### `default` – exploration and statistics (many-to-many)

**Use when**

- You want **all nearby matches**, not just the best one.
- It is fine for one physical object (power pole, street lamp, intersection etc) to be attached to **many** sidewalk features.
- You are doing **exploratory analysis**, QA, or generating statistics.

**Typical OSW example – all light poles near sidewalks**

> For each sidewalk edge, list **all** light poles that lie within 4 m of the edge, and only along the “middle” of the edge (between 20% and 90% of its length), then attach detailed pole attributes.

```json
{
    "target_dataset_id": "791a65c8-2887-4df4-b624-7ebe5a4d30d0",
    "target_dimension": "edge",
    "source_dataset_id": "018c3608-0520-4dec-a625-b3942711ebfe",
    "source_dimension": "node",
    "join_condition": "ST_DWithin(geometry_target, geometry_source, 4) AND (ST_LineLocatePoint(geometry_target, geometry_source) BETWEEN 0.2 AND 0.9)",
    "join_filter_target": "",
    "join_filter_source": "",
    "aggregate": [
        "ARRAY_AGG(ext:unit_id) as SDOT_pole_unit_id",
        "ARRAY_AGG(ext:subtypecd) as SDOT_subtypecd",
        "ARRAY_AGG(ext:pole_height) as SDOT_pole_height",
        "ARRAY_AGG(ext:pole_asset_id) as SDOT_pole_asset_id",
        "ARRAY_AGG(ext:pole_HasStreetlight) as SDOT_pole_HasStreetlight"
    ],
    "assignment_method": "default"
}
```

**How to interpret**

- Each sidewalk edge will have arrays listing **all** poles that are close to that edge and fall along the interior (20–90%) of the edge geometry.
- The same physical pole may appear under multiple edges if it is close enough to more than one edge.

Use `default` when your question is roughly: **“What exists around each feature?”**

---

##### `exclusive` – strict one-to-one assignments

**Use when**

- You need a **clean 1–1 mapping** between datasets:
    - Each curb ramp must belong to **one** sidewalk edge or crossing.
    - Each target should not share a source that another target also owns.
- You are building a **routing or network model** and want to avoid double-counting sources.

**Typical OSW example – assign each curb ramp to a single best sidewalk node**

> For each curb ramp node, choose exactly one “host” sidewalk node with `barrier='kerb'` within 4 m; avoid assigning the same ramp to multiple nodes.

```json
{
    "target_dataset_id": "52945d79-a0df-4440-8363-73bea8e1882a",
    "target_dimension": "node",
    "source_dataset_id": "d286d472-52c3-481b-bf74-a1289091a422",
    "source_dimension": "node",
    "join_condition": "ST_DWithin(geometry_target, geometry_source, 4)",
    "join_filter_target": "barrier='kerb'",
    "join_filter_source": "barrier='kerb'",
    "aggregate": [
        "ARRAY_AGG(_id) as SDOT_curb_ramp_id",
        "ARRAY_AGG(ext:unit_id) as SDOT_curb_ramp_unit_id",
        "ARRAY_AGG(ext:ramp_width_mt) as SDOT_curb_ramp_width"
    ],
    "assignment_method": "exclusive"
}
```

**How to interpret**

- Each sidewalk node with `barrier='kerb'` will have attributes derived from **at most one** ramp node.
- Each ramp node is assigned to **at most one** sidewalk node.

Use `exclusive` when your question is roughly: **“Who is the single owner/host of this feature?”**

---

##### `shared` – shared infrastructure (one-to-many)

**Use when**

- Each target should pick its **best** source (usually the closest).
- It is realistic for the same physical object to serve **multiple** targets:
    - One curb ramp provides access to several nearby edges.
- You want just **one chosen source per target**, but allow reuse of that source.

**Typical OSW example – each intersection node gets its nearest intersection record, intersections can be shared**

> For each node in the sidewalk network representing an intersection, attach information from the nearest intersection record (within 20 m). The same intersection record may serve multiple sidewalks.

```json
{
    "target_dataset_id": "7deb13ce-8af7-4198-98c7-b63fd66def10",
    "target_dimension": "edge",
    "source_dataset_id": "f46995c3-0947-41b1-a2f3-3ca2d4dbf65e",
    "source_dimension": "node",
    "join_condition": "ST_DWithin(geometry_target, geometry_source, 20)",
    "join_filter_target": "",
    "join_filter_source": "",
    "aggregate": [
        "ARRAY_AGG(_id) as intersection_id",
        "ARRAY_AGG(ext:unitdesc) as intersection_unit_desc"
    ],
    "assignment_method": "shared"
}
```

**How to interpret**

- Each target sidewalk is linked to the **closest** intersection record (if any).
- The same intersection record can be the chosen record for many different sidewalks.

Use `shared` when your question is roughly: **“What is the main facility or record serving this location, even if it serves others too?”**

---

### Composing your own spatial joins

When building a new request, think in three steps:

- **Choose datasets and dimensions**
    - **Target** (`target_dataset_id`, `target_dimension`): what you want to enrich (e.g., `edge`, `node`, `zone`).
    - **Source** (`source_dataset_id`, `source_dimension`): what provides attributes (e.g., `point` for ramps, `polygon` for buildings, `edge` for network-to-network).

- **Define spatial relationship and filters**
    - `join_condition` examples:
        - `"ST_DWithin(geometry_target, geometry_source, 5)"` – within 5 m.
        - `"ST_Intersects(ST_Buffer(geometry_target, 2), geometry_source)"` – within a corridor around an edge.
    - `join_filter_target` / `join_filter_source` examples:
        - `"highway='footway' AND footway='sidewalk'"`, `"barrier='kerb'"`, `"highway='street_lamp'"`, `"amenity='bench'"`.

- **Define aggregates and assignment method**
    - `aggregate` examples:
        - `"ARRAY_AGG(highway) as lamps"`,
        - `"min(ramp_width_mt) as min_ramp_width"`,
        - `"count(*) as ramp_count"`.
    - `assignment_method`:
        - **`default`** – keep **all** matching sources (exploration, statistics, QA).
        - **`exclusive`** – enforce **one-to-one** relationships (strict network models).
        - **`shared`** – pick **one best source per target** but allow sources to be reused (shared facilities).

By combining above these input parts, you can compose your own spatial joins tailored to OSW sidewalk and pedestrian accessibility use cases.

---

_Return to [Jobs](index.md)._

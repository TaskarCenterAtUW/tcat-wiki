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

![Spatial Join form](../../../../resources/images/tdei-portal/user-manual/jobs/spatial-join-light.png#only-light)
![Spatial Join form](../../../../resources/images/tdei-portal/user-manual/jobs/spatial-join-dark.png#only-dark)

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

_Return to [Jobs](index.md)._

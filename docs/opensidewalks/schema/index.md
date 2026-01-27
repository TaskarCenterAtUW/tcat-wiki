---
title: OpenSidewalks Schema
tags:
    - Guide
    - External
    - Developer
    - OSW 0.3
---

<!-- @format -->

## OpenSidewalks Schema

The [OpenSidewalks Schema](https://github.com/OpenSidewalks/OpenSidewalks-Schema) is an open pedestrian transportation network data standard for describing and sharing pedestrian network and pedestrian network-adjacent data. The OpenSidewalks Schema promotes an explicit network (graph) model wherein its primary data entities can be deterministically transformed into graph Edges and graph Nodes.

Therefore, OpenSidewalks Schema data represents a traversable and graph-analyzable network of (conditional) pedestrian paths like sidewalks, street crossings, some streets, and other paths, as well as metadata representing potential barriers.

The OpenSidewalks Schema is explicitly a _network schema_: its primary features are defined and interpreted as elements of a network (or graph), i.e. Nodes and Edges. Therefore, OpenSidewalks Schema data is understood not only as a set of features describing pedestrian infrastructure, but as _connected elements_ of a pedestrian network.

The OpenSidewalks Schema draws from and is intended to be largely compatible with OpenStreetMap data, though it is possible to create OpenSidewalks Schema data not derived from OpenStreetMap.

### Transportation Data Exchange Initiative

Validation, ingestion, and downstream use of the OpenSidewalks Schema are supported by tooling developed and maintained through the [Transportation Data Exchange Initiative](../../tdei/index.md) ([TDEI](https://tdei.cs.washington.edu/)).

TDEI provides both user-facing interfaces and programmatic APIs that enable schema validation, quality assurance, dataset management, and access for OpenSidewalks-compliant data. These tools support data producers, stewards, and consumers in publishing and using standardized pedestrian infrastructure datasets at scale.

#### Metrics

As of January 2026, the TDEI system hosts **over 5600 complete OpenSidewalks-validated and vetted datasets**, representing more than **10.5 million crossings** and almost **400,000 miles of sidewalks**, with ongoing updates and expansion. These datasets have passed schema validation and TDEI quality control workflows prior to publication. For current metrics of OpenSidewalks data in the TDEI, please refer to the [TDEI Performance Dashboard](https://metrics.tdei.us/).

#### Validation

An OpenSideWalks Schema validator is available as a Python library and as a Job Type in the TDEI Portal:

- Library:
    - [PyPI: python-osw-validation](https://pypi.org/project/python-osw-validation/)

    - [GitHub: TaskarCenterAtUW/TDEI-python-lib-osw-validation](https://github.com/TaskarCenterAtUW/TDEI-python-lib-osw-validation)

- Service:
    - [TDEI Portal: Create Job](https://portal.tdei.us/CreateJob): "OSW - Validate" (Dataset-Validate)

    - [GitHub: TaskarCenterAtUW/TDEI-python-osw-validation](https://github.com/TaskarCenterAtUW/TDEI-python-osw-validation)

### OpenSidewalks Schema Entities

The OpenSidewalks Schema defines network and non-network data using a set of vector geometrical entity types, each of which has an associated geometry type compatible with either the Point, LineString, or Polygon specification of [Simple Feature Access](https://www.ogc.org/standards/sfa), fields that uniquely define the entity type (in combination), optional topological information, and optional key-value pair [metadata fields](#metadata-fields) defined on a per-type basis.

#### Entity Categories

There are currently two major categories of OpenSidewalks Schema entities: Core Entities and Adjacent Entities.

##### 1. Core Entities

Core Entities are the traversable entities which make up the OpenSidewalks pedestrian network.

There are three types of core entity models:

- Nodes
- Edges
- Zones

Nodes, Edges, and Zones are geometrical features (OGC Points, LineStrings and Polygons, respectively) with network primitives defined such that a network (or graph) can be constructed purely from their metadata. Examples of each entity model:

- Node: a raise curb.
- Edge: a sidewalk.
- Zones: a square or plaza.

###### Nodes

Nodes are Point features (as defined in [Simple Feature Access](https://www.ogc.org/standards/sfa)) that also contain metadata to identify them as network (graph) vertices. They must have a unique (within the dataset) `_id` field. Therefore, the set of network vertices in the dataset could be summarized as a set of these `_id` field values, consistent with the definition of vertices within a graph in graph theory. As a result of storing these vertex identifiers, Nodes may be placed within a traversable graph using only metadata, not spatial inference.

###### Edges

Edges are linear features that also contain metadata to identify them as network (graph) Edges. They must have two Node-referencing fields: `_u_id` and `_v_id`, which mean "this linear feature begins at the Node with `_id` of `_u_id` and ends at the Node with `_id` of `_v_id`. Therefore, a network (graph) may be constructed from a set of Nodes and Edges directly from metadata. Outside of the graph representation, Edges must have a unique (within the dataset) `_id` field.

Note that Edges are directional features: they start at one Node and end at one Node. The data they represent is directional as well: their geospatial data must start at one location and end at another and Edges often have fields like `incline` that only have meaning when direction is understood: a positive incline value is uphill while a negative incline value is downhill. However, this does not mean that datasets must be curated with both "forward" (`u` to `v`) Edges and "reverse" (`v` to `u`) Edges: any "reverse" Edge can be inferred during graph creation.

###### Zones

Zones are Polygon features that also contain metadata to identify them as network (graph) Edges. They must have a list of Node references: `_w_id`, which mean "this 2-dimensional Polygon feature consists of a complete graph with every pair of distinct Nodes in `_w_id` connected by a unique Edge.

Note that this would yield $k(k-1)/2$ Edges for a Zone comprised of $k$ Nodes.

##### 2. Adjacent Entities

Adjacent Entities are pedestrian network-adjacent entities that help describe the surrounding environment of the pedestrian network and can be used to augment the traversable network with important information. For example, a blind user would benefit from knowing that the footway they are using is adjacent to vegetation on their right side and a lake on their left side, or a park visitor would want to know where benches are located along their walk. Adjacent entities are not required for producing a valid OpenSidewalks dataset.

There are three types of adjacent entity models:

- Points
- Lines
- Polygons

Points, Lines, and Polygons are solely geometrical OGC features and they lack network metadata: their relationship to other members of the dataset is spatial. Adjacent entities are features relevant to the pedestrian network that are nevertheless not represented as elements of it: they are nearby and useful for producing descriptions, flagging potential barriers, etc.

Examples of each adjacent entity model:

- Point: a fire hydrant.
- Line: a wall or a fence.
- Polygon: a planter.

OpenSidewalks schema includes some Adjacent Entities which we found valuable to the pedestrian experience and are readily available through community contributions on OpenStreetMap. Other Custom Entities can also be included in an OpenSidewalks dataset and subsequently spatially merged with the Core Entities defined in the schema.

###### Points

Points are features that are geometrically defined by a single latitude-longitude pair: a point on the planet. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes and Edges), but they are still highly relevant to the physical pedestrian network. Points may be considered part of the real physical pedestrian network, but aren't appropriate as elements of the network described by the OpenSidewalks Schema. All Points must have a unique `_id` field.

###### Lines

Lines are features that are geometrically defined by a series of coordinates forming a LineString. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes, Edges and Zones), but they are still highly relevant to the physical pedestrian network. All Lines must have a unique `_id` field.

###### Polygons

Polygons describe 2-dimensional areas which are adjacent to pedestrian paths. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes, Edges and Zones), but they are still highly relevant to the physical pedestrian network. All Polygons must have a unique `_id` field.

##### 3. Custom Entities

Custom Entities are user-defined features that extend the OpenSidewalks Schema beyond the predefined Core and Adjacent categories. They enable incorporation of bespoke data layers while maintaining schema consistency. Custom Entities can take one of three geometry types:

- [Points](#custom-points)
- [Lines](#custom-lines)
- [Polygons](#custom-polygons)

#### Entity Attributes

Every entity has a set of defining attributes:

- **_geometry type_** that define the OGC geospatial type of the feature.
- **_identifying fields_** that must be matched to infer the entity type.
- **_optional fields_** that describe additional attributes of the entity.
- **_additional fields_** that describe attributes of the entity which have not been captured by the OpenSidewalks schema. Any _additional fields_ must be prefixed with `ext:`.

#### Entity Type Inference

Intended to closely mirror OpenStreetMap entities, OpenSidewalks Schema entities are identified by their set of attributes. Fields that uniquely identify an entity type are called _identifying fields_. In most cases, if an entity has all of the _identifying fields_ specified and a matching _geometry type_, its type is matched. The only exception is for entities whose _identifying fields_ are also a subset of other entities' _identifying fields_, in which case they are identified by (1) having all of the _identifying fields_ listed and a matching _geometry type_ and also (2) **not** any of the _identifying fields_ of subtypes.

#### Metadata Fields

The optional metadata fields that may be populated for OpenSidewalks Schema entities are largely inspired by and compatible with (reading from) OpenStreetMap data.

OpenStreetMap-derived fields represent a standardized and constrained interpretation of OpenStreetMap tags that often represent boolean values as yes/no strings, have unclear enumerated value tags, or allow the use of many different units for distances (e.g., a path's width may be described in meters, centimeters, feet, or other units in OpenStreetMap). The standardization of field types is itself inspired by the OpenMapTiles standard, which is optimized for protobuf-based serialization.

The combination of metadata standardization and network structures make OpenSidewalks data machine-readable and amenable to standardized analysis pipelines.

Additional information on field types can be found in the overview subsection of the fields section.

#### Network Topologies

The OpenSidewalks Schema includes network topological rules for the ways in which network-mappable entities can be connected.

##### Edges only connect end-to-end

While a graph structure may be inferred from Edges via their endpoints, the use of `_u_id` and `_v_id` are preferred. However, Edge entities should still meet end-to-end as they are intended to represent a physically-connected space.

Similarly, no connection is implied when the linear geometries of Edges cross.

##### A road entity and a crossing that intersects with it should share a Node

In addition to the above rule about Edge entities connecting end-to-end, it is considered incorrect for a street crossing to intersect with (cross) associated road entities. Instead, both the road and crossing entities should be split such that endpoints are shared.

##### Crossings do not connect to sidewalk centerlines

The OpenSidewalks Schema defines [Crossings](#crossing) as existing only on the street surface and [Sidewalks](#sidewalk) as describing only the sidewalk centerline. There must therefore always be space between a Sidewalk and a Crossing. A Sidewalk and Crossing should be connected by a plain [Footway](#footway).

##### Curb interfaces and curb ramps are mapped at Edge endpoints

Curb Nodes should be mapped directly at the endpoint(s) of one or more Edge(s): they are potential barriers or accessible infrastructure encountered along a path, so they should be available for inspection during network traversals. In other words, they are often important decision points when simulating a pedestrian moving through the network.

#### Serialization Formats

OpenSidewalks data entities are vector geometries with optional topological data along with metadata that defines the entity type and optional [metadata fields](#metadata-fields) that are mappable to non-nested key-value pairs. As such, OpenSidewalks Schema data can be (de)serialized into a number of tabular and non-tabular GIS and graph formats. There exists both a [reference JSON Schema for a GeoJSON serialization](https://github.com/OpenSidewalks/OpenSidewalks-Schema/blob/main/opensidewalks.schema.json) codebase for the OpenSidewalks Schema as well as a PostgreSQL schema.

#### Coordinate Reference System

OpenSidewalks uses the World Geodetic System 1984 (WGS-84) coordinate system. WGS-84 is a geographic coordinate reference system (CRS) with longitude and latitude units of decimal degrees.

In compliance with the RFC 7946 GeoJSON, OpenSidewalks GeoJSON files will not include a `"crs":` element.

#### OpenSidewalks Dataset Metadata

Each file in the OpenSidewalks dataset will contain the following metadata fields:

- `$schema` (string, required): this field specifies the [schema version](#schema-versions) which the dataset is compliant with and should be used for validation.
- `dataSource` (object, optional): the data source which was used to generate the dataset. This can be OpenStreetMap, aerial imagery, or a dataset provided by an agency or a combination of sources.
- `region` (MultiPolygon, optional): a MultiPolygon capturing the geographical area covered by the OpenSidewalks dataset.
- `dataTimestamp` (date/time, optional): a date/time field stating the freshness of the data used in creating the OpenSidewalks dataset. For example, if aerial imagery was the basis for generating a dataset then the timestamp associated with these images can be used.
- `pipelineVersion` (object, optional): the software and version of the software that was used to generate the dataset.

The following is a sample snippet demonstrating the use of these metadata fields:

```json
{
    "$schema": "https://sidewalks.washington.edu/opensidewalks/0.2/schema.json",
    "dataSource": {
        "name": "OpenStreetMap",
        "copyright": "https://www.openstreetmap.org/copyright",
        "license": "https://opendatacommons.org/licenses/odbl/1-0/"
    },
    "region": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [-122.1369414, 47.6365011],
                    [-122.1431969, 47.6365115],
                    [-122.1431951, 47.6469514],
                    [-122.1430782, 47.6495122],
                    [-122.1429792, 47.6495373]
                ]
            ]
        ]
    },
    "dataTimestamp": "2023-08-08T20:22:00Z",
    "pipelineVersion": {
        "name": "OSWDataPipeline",
        "version": "0.2-beta",
        "url": "https://github.com/TaskarCenterAtUW/OSWDataPipeline/tree/v0.2-beta"
    }
}
```

#### List of Core Entities

##### Nodes

Nodes are features that are geometrically defined by a single latitude-longitude pair: a point on the planet. They are also defined as a part of a pedestrian network: each Node must define an `_id` string field, a unique identifier to which Edges and Zones may refer using their `_u_id`, `_v_id` or `_w_id` fields.

??? abstract "Bare Node"

    <table class="schema-table">
    <tr><td>Description</td><td>A special case of an abstract Node: this is a network (graph) Node description that does not have any special metadata beyond location and the <code>_id</code> field. A Bare Node exists when two Edges meet at a location that is not one of the other Node types. For example, a single sidewalk may be represented by two <a href="#sidewalk">Sidewalk</a> Edges with different <code>width</code> values, split where the width changes. There is no physical feature within the OpenSidewalks Schema at the location of that split: it is just a Bare Node that connects the two Edges together.<br><br>Another way to interpret a Bare Node is in terms of the Edge definition rules: the Nodes referenced by <code>_u_id</code> and <code>_v_id</code> must exist within the dataset, so we must define Nodes wherever Edges meet regardless of whether that point in space has additional metadata.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td>(must have the <code>_id</code> field, like all Nodes)</td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Generic Curb"

    <table class="schema-table">
    <tr><td>Description</td><td>A curb for which a type has not been determined yet or a type could not be determined despite some effort.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=kerb</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#tactile-paving"><code>tactile_paving</code></a></td></tr>
    </table>

??? abstract "Raised Curb"

    <table class="schema-table">
    <tr><td>Description</td><td>A single, designed vertical displacement that separates two Edges. A common example is the curb that separates a street crossing from a sidewalk. This is mapped at the Node where the two Edges meet - on top of the curb is physically located.</td></tr>
    <tr><td>Subtype of</td><td><a href="#generic-curb">Generic Curb</a></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=kerb</code>, <code>kerb=raised</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#generic-curb">optional fields of generic curb</a></td></tr>
    </table>

??? abstract "Rolled Curb"

    <table class="schema-table">
    <tr><td>Description</td><td>A curb interface with a quarter-circle profile: traversing this curb is like going over half of a bump. Located where two Edges meet, physically at the location of the curb itself.</td></tr>
    <tr><td>Subtype of</td><td><a href="#generic-curb">Generic Curb</a></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=kerb</code>, <code>kerb=rolled</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#generic-curb">optional fields of generic curb</a></td></tr>
    </table>

??? abstract "Curb Ramp"

    <table class="schema-table">
    <tr><td>Description</td><td>A curb ramp (curb cut) mapped as a curb interface. Mapped at the location where the two Edges that it connects meet one another.</td></tr>
    <tr><td>Subtype of</td><td><a href="#generic-curb">Generic Curb</a></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=kerb</code>, <code>kerb=lowered</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#generic-curb">optional fields of generic curb</a></td></tr>
    </table>

??? abstract "Flush Curb"

    <table class="schema-table">
    <tr><td>Description</td><td>An indicator that there is no raised curb interface where two Edges meet - i.e. where someone might expect a curb interface, such as where a crossing and footway meet.</td></tr>
    <tr><td>Subtype of</td><td><a href="#generic-curb">Generic Curb</a></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=kerb</code>, <code>kerb=flush</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#generic-curb">optional fields of generic curb</a></td></tr>
    </table>

##### Edges

Edges are Lines (their serializable geometries are representable by LineStrings) intended to represent pedestrian network connections. Edges are often derived from topological data like that stored in OpenStreetMap. All Edges must have a unique `_id` field.

??? abstract "Footway (plain)"

    <table class="schema-table">
    <tr><td>Description</td><td>The centerline of a dedicated pedestrian path that does not fall into any other subcategories.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=footway</code><br><em>(and no <code>footway=*</code> subtag)</em></td></tr>
    <tr><td>Optional Fields</td><td><a href="#width">width</a><br><a href="#surface">surface</a><br><a href="#incline">incline</a><br><a href="#length">length</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#foot">foot</a></td></tr>
    </table>

??? abstract "Sidewalk"

    <table class="schema-table">
    <tr><td>Description</td><td>The centerline of a sidewalk, a designated pedestrian path to the side of a street.</td></tr>
    <tr><td>Subtype of</td><td><a href="#footway">Footway</a></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=footway</code>, <code>footway=sidewalk</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#footway">optional fields of footway</a><br><a href="#description">description</a></td></tr>
    </table>

??? abstract "Crossing"

    <table class="schema-table">
    <tr><td>Description</td><td>(Part of) the centerline of a pedestrian street crossing. A crossing exists only on the road surface itself, i.e. "from curb to curb".<br><br>Because crossings should be connected to the street network, they should be represented by at least two Edges: one from the first curb interface to the street centerline and one from the street centerline to the second curb interface, e.g..<br><br>Crossings should not be connected directly to sidewalk centerlines, as the sidewalk centerline is never the curb interface. Instead, a short footway should connect the two together.</td></tr>
    <tr><td>Subtype of</td><td><a href="#footway">Footway</a></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=footway</code>, <code>footway=crossing</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#footway">optional fields of footway</a><br><a href="#crossing-markings">crossing:markings</a></td></tr>
    </table>

??? abstract "Traffic Island"

    <table class="schema-table">
    <tr><td>Description</td><td>The centerline of a footway traversing a traffic island. Some complex, long, or busy pedestrian crossings have a built-up "island" to protect pedestrians, splitting up the crossing of the street into two or more crossings. As a pedestrian uses this crossing, they will transition across these Edge elements: sidewalk → footway → crossing → traffic island → crossing → footway → sidewalk.</td></tr>
    <tr><td>Subtype of</td><td><a href="#footway">Footway</a></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=footway</code>, <code>footway=traffic_island</code></td></tr>
    <tr><td>Optional Fields</td><td>All <a href="#footway">optional fields of footway</a></td></tr>
    </table>

??? abstract "Pedestrian Road"

    <table class="schema-table">
    <tr><td>Description</td><td>The centerline of a road or an area mainly or exclusively for pedestrians in which some vehicle traffic may be authorized.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=pedestrian</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#width">width</a><br><a href="#surface">surface</a><br><a href="#incline">incline</a><br><a href="#length">length</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#foot">foot</a></td></tr>
    </table>

??? abstract "Steps"

    <table class="schema-table">
    <tr><td>Description</td><td>The centerline of a flight of steps on footways and paths.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=steps</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#width">width</a><br><a href="#surface">surface</a><br><a href="#incline">incline</a><br><a href="#length">length</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#stepcount">step_count</a><br><a href="#climb">climb</a><br><a href="#foot">foot</a></td></tr>
    </table>

??? abstract "Living Street"

    <table class="schema-table">
    <tr><td>Description</td><td>A street designed with the interests of pedestrians and cyclists in mind by providing enriching and experiential spaces.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=living_street</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#width">width</a><br><a href="#surface">surface</a><br><a href="#incline">incline</a><br><a href="#length">length</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#foot">foot</a></td></tr>
    </table>

??? abstract "Motor Vehicle Roads"

    While OpenSidewalks schema is centered around the pedestrian experience and accessibility within the pedestrian network, the inclusion of roads as core entities in the schema is justified because:

    1. In some areas due to the lack of sidewalks, a pedestrian has to use a road to reach their destination.
    2. Sidewalks and crossings are typically referenced by pedestrians in relation to roads, i.e. "Use the Sidewalk East of Main St.", "Turn left and cross Broadway".
    3. A pedestrian's safety and environment is greatly impacted by their adjacency to a particular road. For example, a wheelchair user may choose to avoid crossing busy roads for their safety unless they have to.

    In order to simplify the job of OpenSidewalks consuming applications when attempting to route pedestrians, we have included a [foot](#foot) field in all Edges and Zones to indicate whether an entity is safe to traverse by a pedestrian. We recommend applications clearly communicate the risk to pedestrians if they route users on entities with missing [foot](#foot) field or with `foot=no`.

    ??? abstract "Primary Street"

        <table class="schema-table">
        <tr><td>Description</td><td>The centerline of a major highway.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=primary</code></td></tr>
        <tr><td>Optional Fields</td><td><a href="#width">width</a><br><a href="#surface">surface</a><br><a href="#incline">incline</a><br><a href="#length">length</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#foot">foot</a></td></tr>
        </table>

    ??? abstract "Secondary Street"

        <table class="schema-table">
        <tr><td>Description</td><td>The centerline of a secondary highway: not a major highway, but forms a major link in the national route network.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=secondary</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Tertiary Street"

        <table class="schema-table">
        <tr><td>Description</td><td>A road linking small settlements, or the local centers of a large town or city.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=tertiary</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Residential Street"

        <table class="schema-table">
        <tr><td>Description</td><td>A residential street.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=residential</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Service Road"

        <table class="schema-table">
        <tr><td>Description</td><td>A road intended for service use.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=service</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Driveway"

        <table class="schema-table">
        <tr><td>Description</td><td>The centerline of a driveway. Typically connects a residence or business to another road.</td></tr>
        <tr><td>Subtype of</td><td><a href="#service-road">Service road</a></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=service</code>, <code>service=driveway</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Alley"

        <table class="schema-table">
        <tr><td>Description</td><td>The centerline of an alley. An alley is usually located between properties and provides access to utilities and private entrances.</td></tr>
        <tr><td>Subtype of</td><td><a href="#service-road">Service road</a></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=service</code>, <code>service=alley</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Parking Aisle"

        <table class="schema-table">
        <tr><td>Description</td><td>The centerline of a subordinated way in a parking lot: vehicles drive on parking aisles to reach parking spaces in a parking lot.</td></tr>
        <tr><td>Subtype of</td><td><a href="#service-road">Service road</a></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=service</code>, <code>service=parking_aisle</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Unclassified Road"

        <table class="schema-table">
        <tr><td>Description</td><td>A minor public road, typically at the lowest level of whatever administrative hierarchy is used in that jurisdiction.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=unclassified</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

    ??? abstract "Trunk Road"

        <table class="schema-table">
        <tr><td>Description</td><td>A high-performance or high-importance road that doesn't meet the requirements for motorway, but is not classified as highway=primary either.</td></tr>
        <tr><td>Subtype of</td><td><em>None</em></td></tr>
        <tr><td>Geometry</td><td>LineString</td></tr>
        <tr><td>Identifying Fields</td><td><code>highway=trunk</code></td></tr>
        <tr><td>Optional Fields</td><td>All <a href="#primary-street">optional fields of a primary street</a>.</td></tr>
        </table>

#### Zones

Zones are features that are geometrically defined by a Polygon (a closed ring of coordinates). They are also defined as a part of a pedestrian network: each Zone must define an `_id` string field, a unique identifier, and a list (`_w_id`) of Node `_id`s that define the Zone's boundary.

??? abstract "Pedestrian Zone"

    <table class="schema-table">
    <tr><td>Description</td><td>An area where pedestrians can travel freely in all directions.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Polygon</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=pedestrian</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#surface">surface</a><br><a href="#description">description</a><br><a href="#name">name</a><br><a href="#foot">foot</a></td></tr>
    </table>

### List of Adjacent Entities

#### Points

Points are features that are geometrically defined by a single latitude-longitude pair: a point on the planet. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes and Edges), but they are still highly relevant to the physical pedestrian network. All Points must have a unique `_id` field.

??? abstract "Power Pole"

    <table class="schema-table">
    <tr><td>Description</td><td>A power pole. Often made of wood or metal, they hold power lines.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>power=pole</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Fire Hydrant"

    <table class="schema-table">
    <tr><td>Description</td><td>A fire hydrant - where fire response teams connect high-pressure hoses.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>emergency=fire_hydrant</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Bench"

    <table class="schema-table">
    <tr><td>Description</td><td>A bench - a place for people to sit; allows room for several people.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>amenity=bench</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Bollard"

    <table class="schema-table">
    <tr><td>Description</td><td>A bollard - a solid pillar or pillars made of concrete, metal, plastic, etc., and used to control traffic.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=bollard</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Manhole"

    <table class="schema-table">
    <tr><td>Description</td><td>A manhole - a hole with a cover that allows access to an underground service location, just large enough for a human to climb through.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>man_made=manhole</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Street Lamp"

    <table class="schema-table">
    <tr><td>Description</td><td>A street lamp - a street light, lamppost, street lamp, light standard, or lamp standard: a raised source of light above a road, which is turned on or lit at night.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>highway=street_lamp</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Waste Basket"

    <table class="schema-table">
    <tr><td>Description</td><td>A waste basket - a single small container for depositing garbage that is easily accessible for pedestrians.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>amenity=waste_basket</code></td></tr>
    <tr><td>Optional Fields</td><td><em>None</em></td></tr>
    </table>

??? abstract "Tree"

    <table class="schema-table">
    <tr><td>Description</td><td>A tree - a tall, woody plant with branches emanating from a central trunk.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><code>natural=tree</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#leaf-cycle">leaf_cycle</a><br><a href="#leaf-type">leaf_type</a></td></tr>
    </table>

##### Lines

Lines are features that are geometrically defined by a series of coordinates forming a LineString. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes, Edges and Zones), but they are still highly relevant to the physical pedestrian network. All Lines must have a unique `_id` field.

??? abstract "Fence"

    <table class="schema-table">
    <tr><td>Description</td><td>A fence is a freestanding structure designed to restrict or prevent movement across a boundary. It is generally distinguished from a wall by the lightness of its construction.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>barrier=fence</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#length">length</a></td></tr>
    </table>

??? abstract "Tree Row"

    <table class="schema-table">
    <tr><td>Description</td><td>A tree row is a line of trees often found along roadways, property lines, or at the edges of farms.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><code>natural=tree_row</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#leaf-cycle">leaf_cycle</a><br><a href="#leaf-type">leaf_type</a><br><a href="#length">length</a></td></tr>
    </table>

#### Polygons

Polygons describe 2-dimensional areas which are adjacent to pedestrian paths. They are explicitly **not** elements of the pedestrian network definition (i.e. the graph structure described by Nodes, Edges and Zones), but they are still highly relevant to the physical pedestrian network. All Polygons must have a unique `_id` field.

??? abstract "Building"

    <table class="schema-table">
    <tr><td>Description</td><td>A building is a man-made structure with a roof, standing more or less permanently in one place.</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Polygon</td></tr>
    <tr><td>Identifying Fields</td><td><a href="#building-1">building</a>=\*</td></tr>
    <tr><td>Optional Fields</td><td><a href="#name">name</a><br><a href="#opening-hours">opening_hours</a></td></tr>
    </table>

??? abstract "Wood"

    <table class="schema-table">
    <tr><td>Description</td><td>Wood - a tree-covered area</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Polygon</td></tr>
    <tr><td>Identifying Fields</td><td><code>natural=wood</code></td></tr>
    <tr><td>Optional Fields</td><td><a href="#leaf-cycle">leaf_cycle</a><br><a href="#leaf-type">leaf_type</a><br><a href="#name">name</a><br><a href="#opening-hours">opening_hours</a></td></tr>
    </table>

#### List of Custom Entities

##### Custom Point

??? abstract "Custom Point"

    <table class="schema-table">
    <tr><td>Description</td><td>A custom point is a user-defined Point feature. It can represent any custom-location marker (e.g., a survey marker).</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Point</td></tr>
    <tr><td>Identifying Fields</td><td><em>None</em></td></tr>
    <tr><td>Optional Fields</td><td>Additional fields (ext: prefixed)</td></tr>
    </table>

##### Custom Line

??? abstract "Custom Line"

    <table class="schema-table">
    <tr><td>Description</td><td>A custom line is a user-defined LineString feature. It can represent any custom path or linear infrastructure (e.g., temporary detour route).</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>LineString</td></tr>
    <tr><td>Identifying Fields</td><td><em>None</em></td></tr>
    <tr><td>Optional Fields</td><td>Additional fields (ext: prefixed)</td></tr>
    </table>

##### Custom Polygon

??? abstract "Custom Polygon"

    <table class="schema-table">
    <tr><td>Description</td><td>A custom polygon is a user-defined Polygon feature. It can represent any custom area or zone (e.g., event footprint).</td></tr>
    <tr><td>Subtype of</td><td><em>None</em></td></tr>
    <tr><td>Geometry</td><td>Polygon</td></tr>
    <tr><td>Identifying Fields</td><td><em>None</em></td></tr>
    <tr><td>Optional Fields</td><td>Additional fields (ext: prefixed)</td></tr>
    </table>

#### Fields

##### Fields Overview

OpenSidewalks Schema fields are typed key-value pairs. Keys are always strings and values can be any of a specific set. Value types include:

- `boolean`: `true` or `false`
- `text`: unlimited length string
- `enum`: a set of enumerated values designated by strings
- `integer`: an integer
- `numeric`: a number, either integer or decimal
- `opening_hours`: serialized as a string, a specialized format for describing when a facility or asset is "open", as in accessible to the public.

#### List of fields

??? abstract "description"

    <table class="schema-table">
    <tr><td>Description</td><td>This may be a field inferred from other data. A free form text field for describing an Edge, which may be pre-encoded in relevant pedestrian Edges to assist with routing, instructing, or investigation of map features; for example, a description of the sidewalk in relation to a nearby street ("NE of Main St.") or other short (1-3 sentences) textual information not directly available in the schema, such as "this path is muddy when wet." Note that because description data are unstructured, they can only be interpreted individually by people and should not be considered a dumping ground for extra data.</td></tr>
    <tr><td>Value type</td><td>text</td></tr>
    </table>

??? abstract "name"

    <table class="schema-table">
    <tr><td>Description</td><td>The (semi-)official name of an entity. <em>Not</em> a description of the entity. For example, this would be the street name for a street path or a specially-designated name for a famous footpath. <code>name="The [X] trail"</code>, for example.</td></tr>
    <tr><td>Value type</td><td>text</td></tr>
    </table>

??? abstract "incline"

    <table class="schema-table">
    <tr><td>Description</td><td>The estimated incline over a particular path, i.e. slope, i.e. grade, i.e. rise over run. If derived from OpenStreetMap data, this is the maximum incline over the path. If derived from DEM data, it is more likely to be an underestimation. Positive values indicate an uphill climb while negative are downhill. For example, a 45 degree downhill value for incline would be -1.0. For steps, you can use "up" or "down" to indicate the direction of the climb relative to the direction of the Edge.</td></tr>
    <tr><td>Value type</td><td>numeric</td></tr>
    </table>

??? abstract "surface"

    <table class="schema-table">
    <tr><td>Description</td><td>The surface material of the path. Derived directly from the surface tag from OpenStreetMap.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>asphalt</em><br>- <em>concrete</em><br>- <em>gravel</em><br>- <em>grass</em><br>- <em>paved</em><br>- _paving_stones_<br>- <em>unpaved</em><br>- <em>dirt</em><br>- _grass_paver_</td></tr>
    </table>

??? abstract "length"

    <table class="schema-table">
    <tr><td>Description</td><td>This is the calculated length of the way, in meters, according to the Haversine formula (Great-Circle Distance). This calculation is typically left up to consumers of geometry data, as the geometry is, itself, furnished for geometrical analysis. This is likely how AccessMap should also handle these data, but for now length is precalculated.</td></tr>
    <tr><td>Value type</td><td>numeric</td></tr>
    </table>

??? abstract "width"

    <table class="schema-table">
    <tr><td>Description</td><td>The width of an Edge in meters.</td></tr>
    <tr><td>Value type</td><td>numeric</td></tr>
    </table>

??? abstract "tactile_paving"

    <table class="schema-table">
    <tr><td>Description</td><td>A field for whether a curb has a tactile (textured) surface. Tactile paving is a system of textured ground surface indicators found on footpaths, stairs and public transportation platforms to assist pedestrians who are blind or visually impaired. A tactile paving area has a surface that is easy to detect using a long cane, typically because it is rougher than the surrounding surface area or has an embossed pattern.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>yes</em><br>- <em>no</em><br>- <em>contrasted</em>: Where there is a tactile paving which contrast is at least 70% the colour of the ground (white if the ground is black and vice-versa).<br>- <em>primitive</em>: Where any water drain or decorative tactile element can be used for orientation accidentally, but no typical tactile ground elements are used.</td></tr>
    </table>

??? abstract "crossing:markings"

    <table class="schema-table">
    <tr><td>Description</td><td>Whether a pedestrian street crossing has ground markings (and, optionally, what type of markings exist). When derived from OpenStreetMap data, the crossing:markings field may be derived not only from the identical <code>crossing:markings</code> tag in OpenStreetMap, but from any unambiguous tags in the problematic <code>crossing=*</code> tag, such as <code>crossing=marked</code> --> <code>crossing:markings=yes</code> and <code>crossing=unmarked</code> --> <code>crossing:markings=no</code>, and <code>crossing=zebra</code> --> <code>crossing:markings=yes</code>.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>yes</em>: The crossing has surface markings but the type is unspecified.<br>- <em>no</em>: The crossing has no surface markings.<br>- <em>surface</em>: There is a surface change but no distinct markings.<br>- <em>lines</em>: There are only two parallel lines to indicate the outline of the crossing.<br>- <em>lines:paired</em>: The same as <code>crossing:markings=lines</code> but each line is actually two very-close parallel lines (for a total of 4 lines).<br>- <em>dashes</em>: There are only two parallel dashed lines to indicate the outline of the crossing.<br>- <em>dots</em>: There are only two parallel dotted lines (square/round markings with significant distance between them) to indicate the outline of the crossing.<br>- <em>zebra</em>: The crossing is only marked by regularly spaced bars along its length.<br>-zebra:double: The same as <code>crossing:markings=zebra</code> but there are two sets of regularly spaced bars with a small gap between them.<br>- <em>zebra:paired</em>: The same as <code>crossing:markings=zebra</code> but each bar is made up of two smaller bars (i.e. there's a small gap between smaller bars).<br>- <em>zebra:bicolour</em>: The same as <code>crossing:markings=zebra</code> but there are the bars and gaps are made of two alternating colors.<br>- <em>ladder</em>: The same as combining <code>crossing:markings=zebra</code> and <code>crossing:markings=lines</code>: horizontal bars but with linear outlines enclosing the crossing.<br>- <em>skewed</em>: The same as <code>crossing:markings=ladder</code> but the horizontal bars are at a slight diagonal (~30 degree shift) - they're skewed.<br>- <em>ladder:paired</em>: The same as <code>crossing:markings=ladder</code> but the horizontal bars are actually made up of two very-close smaller bars.<br>- <em>rainbow</em>: A crossing with rainbow colors, other than in zebra pattern or lines along the crossing.<br>- <em>lines:rainbow</em>: Rainbow colored lines along the crossing.<br>- <em>zebra:rainbow</em>: A zebra crossing with rainbow colors.<br>- <em>ladder:skewed</em>: Two lines orthogonal to the direction of the roadway with diagonal bars connecting the two lines.<br>- <em>pictograms</em>: Painted pictogram(s) of pedestrian and/or bicycle (with or without arrows)</td></tr>
    </table>

??? abstract "step_count"

    <table class="schema-table">
    <tr><td>Description</td><td>Can be added to indicate the number of steps</td></tr>
    <tr><td>Value type</td><td>integer</td></tr>
    </table>

??? abstract "climb"

    <table class="schema-table">
    <tr><td>Description</td><td>For steps, can be used to indicate the direction of the climb relative to the direction of the Edge</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>up</em>: when a way rises upward <em>in the direction</em> of the Edge.<br>- <em>down</em>: when a way rises upward <em>against the direction</em> of the Edge.</td></tr>
    </table>

??? abstract "building"

    <table class="schema-table">
    <tr><td>Description</td><td>This field is used to mark a given entity as a building</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    </table>

    **Enumerated Values:**

    ??? note "Accommodation"

        <table class="schema-table">
        <tr><td>apartments</td><td>A building arranged into individual dwellings, often on separate floors. May also have retail outlets on the ground floor.</td></tr>
        <tr><td>barracks</td><td>Buildings built to house military personnel or laborers.</td></tr>
        <tr><td>bungalow</td><td>A single-storey detached small house, Dacha.</td></tr>
        <tr><td>cabin</td><td>A cabin is a small, roughly built house usually with a wood exterior and typically found in rural areas.</td></tr>
        <tr><td>detached</td><td>A detached house, a free-standing residential building usually housing a single family.</td></tr>
        <tr><td>dormitory</td><td>A shared building intended for college/university students (not a share room for multiple occupants as implied by the term in British English).</td></tr>
        <tr><td>farm</td><td>A residential building on a farm (farmhouse). For other buildings see below building=farm_auxiliary, building=barn, etc.</td></tr>
        <tr><td>ger</td><td>A permanent or seasonal round yurt or ger.</td></tr>
        <tr><td>hotel</td><td>A building designed with separate rooms available for overnight accommodation.</td></tr>
        <tr><td>house</td><td>A dwelling unit inhabited by a single household (a family or small group sharing facilities such as a kitchen). Houses forming half of a semi-detached pair, or one of a row of terraced houses, should share at least two Nodes with joined neighbours, thereby defining the party wall between the properties.</td></tr>
        <tr><td>houseboat</td><td>A boat used primarily as a home.</td></tr>
        <tr><td>residential</td><td>A general tag for a building used primarily for residential purposes. Where additional detail is available consider using 'apartments', 'terrace', 'house', 'detached' or 'semidetached_house'.</td></tr>
        <tr><td>semidetached_house</td><td>A residential house that shares a common wall with another on one side. Typically called a "duplex" in American English.</td></tr>
        <tr><td>static_caravan</td><td>A mobile home (semi)permanently left on a single site.</td></tr>
        <tr><td>stilt_house</td><td>A building raised on piles over the surface of the soil or a body of water.</td></tr>
        <tr><td>terrace</td><td>A single way used to define the outline of a linear row of residential dwellings, each of which normally has its own entrance, which form a terrace ("row-house" or "townhouse" in North American English). Consider defining each dwelling separately using 'house'.</td></tr>
        <tr><td>tree_house</td><td>An accommodation, often designed as a small hut, sometimes also as a room or small apartment. Built on tree posts or on a natural tree. A tree house has no contact with the ground. Access via ladders, stairs or bridgeways.</td></tr>
        <tr><td>trullo</td><td>A stone hut with a conical roof.</td></tr>
        </table>

    ??? note "Commercial"

        <table class="schema-table">
        <tr><td>commercial</td><td>A building for non-specific commercial activities, not necessarily an office building. Use 'retail' if the building consists primarily of shops.</td></tr>
        <tr><td>industrial</td><td>A building for industrial purposes. Use warehouse if the purpose is known to be primarily for storage/distribution.</td></tr>
        <tr><td>kiosk</td><td>A small one-room retail building.</td></tr>
        <tr><td>office</td><td>An office building.</td></tr>
        <tr><td>retail</td><td>A building primarily used for selling goods that are sold to the public.</td></tr>
        <tr><td>supermarket</td><td>A building constructed to house a self-service large-area store.</td></tr>
        <tr><td>warehouse</td><td>A building primarily intended for the storage or goods or as part of a distribution system.</td></tr>
        </table>

    ??? note "Religious"

        <table class="schema-table">
        <tr><td>cathedral</td><td>A building that was built as a cathedral.</td></tr>
        <tr><td>chapel</td><td>A building that was built as a chapel.</td></tr>
        <tr><td>church</td><td>A building that was built as a church.</td></tr>
        <tr><td>kingdom_hall</td><td>A building that was built as a Kingdom Hall.</td></tr>
        <tr><td>monastery</td><td>A building constructed as monastery. Often, monasteries consist of several distinct buildings with specific functions.</td></tr>
        <tr><td>mosque</td><td>A building erected as mosque.</td></tr>
        <tr><td>presbytery</td><td>A building where priests live and work.</td></tr>
        <tr><td>religious</td><td>Unspecific building related to religion. Prefer more specific values if possible.</td></tr>
        <tr><td>shrine</td><td>A building that was built as a shrine.</td></tr>
        <tr><td>synagogue</td><td>A building that was built as a synagogue.</td></tr>
        <tr><td>temple</td><td>A building that was built as a temple.</td></tr>
        </table>

    ??? note "Civic/amenity"

        <table class="schema-table">
        <tr><td>bakehouse</td><td>A building that was built as a bakehouse (i.e. for baking bread).</td></tr>
        <tr><td>bridge</td><td>A building used as a bridge (skyway). To map a gatehouse use building=gatehouse. Don't use this tag just for marking bridges (their outlines).</td></tr>
        <tr><td>civic</td><td>A generic tag for a building created to house some civic amenity, for example community centre, library, toilets, sports centre, swimming pool, townhall etc. See building=public and more specific tags like building=library as well.</td></tr>
        <tr><td>college</td><td>A college building.</td></tr>
        <tr><td>fire_station</td><td>A building constructed as fire station, i.e. to house fire fighting equipment and officers, regardless of current use.</td></tr>
        <tr><td>government</td><td>For government buildings in general, including municipal, provincial and divisional secretaries, government agencies and departments, town halls, (regional) parliaments and court houses.</td></tr>
        <tr><td>gatehouse</td><td>An entry control point building, spanning over a highway that enters a city or compound.</td></tr>
        <tr><td>hospital</td><td>A building erected for a hospital.</td></tr>
        <tr><td>kindergarten</td><td>For any generic kindergarten buildings. Buildings for specific uses (sports halls etc.) should be tagged for their purpose.</td></tr>
        <tr><td>museum</td><td>A building which was designed as a museum.</td></tr>
        <tr><td>public</td><td>A building constructed as accessible to the general public (a town hall, police station, court house, etc.).</td></tr>
        <tr><td>school</td><td>A building erected as school. Buildings for specific uses (sports halls etc.) should be tagged for their purpose.</td></tr>
        <tr><td>toilets</td><td>A toilet block.</td></tr>
        <tr><td>train_station</td><td>A building constructed to be a train station building, including buildings that are abandoned and used nowadays for a different purpose.</td></tr>
        <tr><td>transportation</td><td>A building related to public transport. Note that there is a special tag for train station buildings - building=train_station.</td></tr>
        <tr><td>university</td><td>A university building.</td></tr>
        </table>

    ??? note "Agricultural/plant production"

        <table class="schema-table">
        <tr><td>barn</td><td>An agricultural building that can be used for storage and as a covered workplace.</td></tr>
        <tr><td>conservatory</td><td>A building or room having glass or tarpaulin roofing and walls used as an indoor garden or a sunroom (winter garden).</td></tr>
        <tr><td>cowshed</td><td>A cowshed (cow barn, cow house) is a building for housing cows, usually found on farms.</td></tr>
        <tr><td>farm_auxiliary</td><td>A building on a farm that is not a dwelling (use 'farm' or 'house' for the farm house).</td></tr>
        <tr><td>greenhouse</td><td>A greenhouse is a glass or plastic covered building used to grow plants.</td></tr>
        <tr><td>slurry_tank</td><td>A circular building built to hold a liquid mix of primarily animal excreta (also known as slurry).</td></tr>
        <tr><td>stable</td><td>A building constructed as a stable for horses.</td></tr>
        <tr><td>sty</td><td>A sty (pigsty, pig ark, pig-shed) is a building for raising domestic pigs, usually found on farms.</td></tr>
        <tr><td>livestock</td><td>A building for housing/rising other livestock (apart from cows, horses or pigs covered above), or when the livestock changes.</td></tr>
        </table>

    ??? note "Sports"

        <table class="schema-table">
        <tr><td>grandstand</td><td>The main stand, usually roofed, commanding the best view for spectators at racecourses or sports grounds.</td></tr>
        <tr><td>pavilion</td><td>A sports pavilion usually with changing rooms, storage areas and possibly an space for functions & events. Avoid using this term for other structures called pavilions by architects.</td></tr>
        <tr><td>riding_hall</td><td>A building that was built as a riding hall.</td></tr>
        <tr><td>sports_hall</td><td>A building that was built as a sports hall.</td></tr>
        <tr><td>sports_centre</td><td>A building that was built as a sports centre.</td></tr>
        <tr><td>stadium</td><td>A building constructed to be a stadium building, including buildings that are abandoned and used nowadays for a different purpose.</td></tr>
        </table>

    ??? note "Storage"

        <table class="schema-table">
        <tr><td>allotment_house</td><td>A small outbuilding for short visits in a allotment garden.</td></tr>
        <tr><td>boathouse</td><td>A boathouse is a building used for the storage of boats.</td></tr>
        <tr><td>hangar</td><td>A hangar is a building used for the storage of airplanes, helicopters or space-craft.</td></tr>
        <tr><td>hut</td><td>A hut is a small and crude shelter. Note that this word has two meanings - it may be synonym of building=shed, it may be a residential building of low quality.</td></tr>
        <tr><td>shed</td><td>A shed is a simple, single-storey structure in a back garden or on an allotment that is used for storage, hobbies, or as a workshop.</td></tr>
        </table>

    ??? note "Cars"

        <table class="schema-table">
        <tr><td>carport</td><td>A carport is a covered structure used to offer limited protection to vehicles, primarily cars, from the elements. Unlike most structures a carport does not have four walls, and usually has one or two.</td></tr>
        <tr><td>garage</td><td>A garage is a building suitable for the storage of one or possibly more motor vehicle or similar. See building=garages for larger shared buildings. For an aircraft garage, see building=hangar.</td></tr>
        <tr><td>garages</td><td>A building that consists of a number of discrete storage spaces for different owners/tenants. See also building=garage.</td></tr>
        <tr><td>parking</td><td>Structure purpose-built for parking cars.</td></tr>
        </table>

    ??? note "Power/technical buildings"

        <table class="schema-table">
        <tr><td>digester</td><td>A digester is a bioreactor for the production of biogas from biomass.</td></tr>
        <tr><td>service</td><td>Service building usually is a small unmanned building with certain machinery (like pumps or transformers).</td></tr>
        <tr><td>tech_cab</td><td>Small prefabricated cabin structures for the air-conditioned accommodation of different technology.</td></tr>
        <tr><td>transformer_tower</td><td>A transformer tower is a characteristic tall building comprising a distribution transformer and constructed to connect directly to a medium voltage overhead power line. Quite often the power line has since been undergrounded but the building may still serve as a substation.</td></tr>
        <tr><td>water_tower</td><td>A water tower.</td></tr>
        <tr><td>storage_tank</td><td>Storage tanks are containers that hold liquids.</td></tr>
        <tr><td>silo</td><td>A silo is a building for storing bulk materials.</td></tr>
        </table>

    ??? note "Other buildings"

        <table class="schema-table">
        <tr><td>beach_hut</td><td>A small, usually wooden, and often brightly coloured cabin or shelter above the high tide mark on popular bathing beaches.</td></tr>
        <tr><td>bunker</td><td>A hardened military building.</td></tr>
        <tr><td>castle</td><td>A building constructed as a castle.</td></tr>
        <tr><td>construction</td><td>Used for buildings under construction.</td></tr>
        <tr><td>container</td><td>For a container used as a permanent building. Do not map containers placed temporarily, for example used in shipping or construction.</td></tr>
        <tr><td>guardhouse</td><td>A small building constructed to house guard(s).</td></tr>
        <tr><td>military</td><td>A military building.</td></tr>
        <tr><td>outbuilding</td><td>A less important building near to and on the same piece of land as a larger building.</td></tr>
        <tr><td>pagoda</td><td>A building constructed as a pagoda.</td></tr>
        <tr><td>quonset_hut</td><td>A lightweight prefabricated structure in the shape of a semicircle.</td></tr>
        <tr><td>roof</td><td>A structure that consists of a roof with open sides, such as a rain shelter, and also gas stations.</td></tr>
        <tr><td>ruins</td><td>Frequently used for a house or other building that is abandoned and in poor repair. However, some believe this usage is incorrect, and the tag should only be used for buildings constructed as fake ruins (for example sham ruins in an English landscape garden). See also lifecycle tagging.</td></tr>
        <tr><td>tent</td><td>For a permanently placed tent. Do not map tents placed temporarily.</td></tr>
        <tr><td>tower</td><td>A tower-building.</td></tr>
        <tr><td>windmill</td><td>A building constructed as a traditional windmill, historically used to mill grain with wind power.</td></tr>
        <tr><td>yes</td><td>Use this value where it is not possible to determine a more specific value.</td></tr>
        </table>

??? abstract "opening_hours"

    <table class="schema-table">
    <tr><td>Description</td><td>The opening hours of the entity. This may apply to, for example, a path that is inside a building or the building itself. The value is in OpenStreetMap syntax for the <code>opening_hours</code> tag. See <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours/specification">OpenStreetMap specification</a> on the formatting for this field.</td></tr>
    <tr><td>Value type</td><td>opening_hours</td></tr>
    </table>

??? abstract "foot"

    <table class="schema-table">
    <tr><td>Description</td><td>A field that indicates whether an Edge can be used by pedestrians.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>yes</em>: Roads and other objects where the public has a legally-enshrined right for access on foot<br>- <em>no</em>: Access on foot or by pedestrians is prohibited.<br>- <em>designated</em>: A preferred or designated route for pedestrians.<br>- <em>permissive</em>: Access by pedestrians is permitted but permission may be withdrawn at any time.<br>- _use_sidepath_: Use compulsory parallel footpath instead.<br>- <em>private</em>: indicates that walking is not allowed for general public, but the owner may make exceptions at will.<br>- <em>destination</em>: Transit traffic forbidden for pedestrians, non-transit to a local destination allowed.</td></tr>
    </table>

??? abstract "leaf_cycle"

    <table class="schema-table">
    <tr><td>Description</td><td>A field that describes the phenology of leaves.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>deciduous</em>: Leaves are shed seasonally, typically in autumn.<br>- <em>evergreen</em>: Retains foliage year-round.<br>- <em>mixed</em>: Both deciduous and evergreen trees are present.</td></tr>
    </table>

??? abstract "leaf_type"

    <table class="schema-table">
    <tr><td>Description</td><td>A field that describes the type of leaves.</td></tr>
    <tr><td>Value type</td><td>enum</td></tr>
    <tr><td>Enumerated Values</td><td>- <em>broadleaved</em>: Broad, flat leaves.<br>- <em>leafless</em>: No leaves.<br>- <em>mixed</em>: Multiple trees with different leaf types.<br>- <em>needleleaved</em>: Needle-shaped leaves.</td></tr>
    </table>

### Schema Versions

| Version | Release Date | Link                                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------|--------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.1     | 2023-08-11   | [GitHub](https://github.com/OpenSidewalks/OpenSidewalks-Schema/tree/32dad18) | - Minimal initial beta release of schema to unblock development of schema consuming applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 0.2     | 2024-01-30   | [GitHub](https://github.com/OpenSidewalks/OpenSidewalks-Schema/tree/9338af)  | - Add required `_id` Field to [Edges](#edges)<br>- Update the documentation with regards to the [coordinate reference system](#coordinate-reference-system)<br>- Introduce the concept of [Core Entities](#core-entities) and [Adjacent Entities](#adjacent-entities) (formerly called "Extensions")<br>- Add [Zones](#zones) to [Core Entities](#core-entities)<br>- Add [Lines](#lines) and [Polygons](#polygons) to [Adjacent Entities](#adjacent-entities)<br>- Add [Schema Versions](#schema-versions) and [OpenSidewalks Dataset Metadata](#opensidewalks-dataset-metadata)<br>- Add [Pedestrian Zone](#pedestrian-zone) to [Zones](#zones)<br>- Add [Fence](#fence) to [Lines](#lines)<br>- Add [Building](#building) to [Polygons](#polygons)<br>- Add _additional fields_ to [Entity Attributes](#entity-attributes)<br>- Add [Motor Vehicle Roads](#motor-vehicle-roads) to [Edges](#edges) with justification<br>- Add [Climb](#climb) Field to [Steps](#steps) Edge in addition to the existing [Incline](#incline) Field<br>- Add [Opening Hours](#opening-hours) Field and include it to the existing [Building](#building) Fields<br>- Add [Generic Curb](#generic-curb) entity to [Nodes](#nodes)<br>- Add [Foot](#foot) Field to all [Edges](#edges) and [Zones](#zones)<br>- Change [Entity Type Inference](#entity-type-inference) to include the _geometry type_<br>- Fix lossiness of [Tactile Paving](#tactile-paving) Field<br>- Remove _crossing_ Field in favor of [crossing:markings](#crossing-markings) Field<br>- Add [Living Street](#living-street) to [Edges](#edges)<br>- Add _unclassified road_ to [Motor Vehicle Roads](#motor-vehicle-roads)<br>- Add _trunk road_ to [Motor Vehicle Roads](#motor-vehicle-roads)<br>- Require that the `_id` Field for all entities has at least one character |
| 0.3     | 2025-06-30   | [GitHub](https://github.com/OpenSidewalks/OpenSidewalks-Schema)              | - Add [Custom Points](#custom-points)<br>- Add [Custom Lines](#custom-lines)<br>- Add [Custom Polygons](#custom-polygons)<br>- Add [Tree](#tree) to [Points](#points)<br>- Add [Tree Row](#tree-row) to [Lines](#lines)<br>- Add [Wood](#wood) to [Polygons](#polygons)<br>- Update documentation to improve clarity with regards to [Adjacent Entities](#adjacent-entities) (formerly called "Extensions")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

---

### Guides

OpenSidewalks Schema Guides

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

#### [Core Edges in OSW](core-edges-in-osw.md)

This guide shows how to convert existing sidewalk centerline datasets into OpenSidewalks (OSW) format for upload to the Transportation Data Exchange Initiative (TDEI).

#### [Custom Points in OSW](custom-points-in-osw.md)

This guide shows how to add custom non-routable point features (like bus stops) to an OpenSidewalks dataset using the Custom Points entity type.

#### [OpenSidewalks in OpenStreetMap](osw-in-osm.md)

This guide explains how to make edits to OpenStreetMap following and supporting the OpenSidewalks schema.

---
title: Validation Guide
tags:
    - Guide
    - External
    - User
# exclude-from-parent-guides-list
# exclude-from-main-guides-list
---

<!-- @format -->

## Validation Guide

This guide covers how to validate mapped pedestrian infrastructure tasks in the OSM US Tasking Manager for the [Mappy New Year 2026](index.md) event.

---

### Quick Links

- **Mapping Guide**: [Mapping Guide](mapping-guide.md) (review before validating)
- **Team**: [#26 - OpenSidewalks - Validators](https://tasks.openstreetmap.us/teams/26/membership/)
- **Project**: [#1017 - Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks](https://tasks.openstreetmap.us/projects/1017)

### What is Validation?

Validation is the process of reviewing the edits of other contributors and evaluating the mapped features to ensure they are:

1. **Correctly shaped** - Lines and points placed accurately
2. **Properly aligned** - Features match real-world locations in imagery
3. **Connected** - The pedestrian network links to the road network
4. **Tagged correctly** - Features use the required tags

Validators should have some mapping experience and be familiar with the [Mapping Guide](mapping-guide.md) before validating others' work.

---

### Getting Started

#### 1. Find Tasks Ready for Validation

1. Go to the project: [#1017 - Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks](https://tasks.openstreetmap.us/projects/1017)
2. Select **Contribute** at the bottom right
3. Look for tasks **ready for validation** (blue tiles)
4. Select an already-mapped, blue task and click **Validate selected task**

#### 2. Review Task History

Before validating, check the **History** tab to see:

- Who mapped the task
- Any comments from the mapper
- Previous validation attempts

---

### Validation Checklist

#### 1. Crossings

- [ ] Crossings are drawn as **lines** across streets
- [ ] Each crossing has **curb nodes** at both ends
- [ ] A **middle node** connects the crossing to the road
- [ ] Crossing lines are tagged, at minimum: `highway=footway` + `footway=crossing`
- [ ] Crossing nodes are tagged, at minimum: `highway=crossing`
- [ ] `crossing:markings=yes` or `crossing:markings=no` (or a more detailed value) is set correctly based on imagery

**Common Issues:**

| Issue                          | How to Fix                                   |
|--------------------------------|----------------------------------------------|
| Crossing not connected to road | Drag the middle node to touch the road       |
| Missing curb nodes             | Add `barrier=kerb` + `kerb=*` to endpoints   |
| Wrong marking tag              | Check imagery and update `crossing:markings` |

#### 2. Curbs

- [ ] Curbs are **points** at the edge of the street
- [ ] Curb type matches imagery: `kerb=lowered`, `raised`, or `flush`
- [ ] Curbs are tagged, at minimum: `barrier=kerb`

**Common Issues:**

| Issue                                  | How to Fix                                                                                     |
|----------------------------------------|------------------------------------------------------------------------------------------------|
| Curb directly at sidewalk intersection | Should move curbs to actual location and connect sidewalk to curb via a short sidewalk footway |
| Wrong curb type                        | Check street-level imagery if available                                                        |
| Missing `barrier=kerb`                 | Add the tag to complete the feature                                                            |

#### 3. Sidewalks

- [ ] Sidewalks are drawn as **lines** along the center of the path
- [ ] Sidewalks are tagged, at minimum: `highway=footway` + `footway=sidewalk`
- [ ] Sidewalks connect to service roads (driveways) where they intersect via a node

**Common Issues:**

| Issue                          | How to Fix                             |
|--------------------------------|----------------------------------------|
| Sidewalk not on centerline     | Move nodes to center the line          |
| Missing connection to driveway | Add a shared node where they intersect |

#### 4. Connectors (Crossing Links)

- [ ] Short lines connect curbs to sidewalk centerlines
- [ ] Connectors are tagged: `highway=footway` + `footway=sidewalk` + (optional) `crossing_link=yes`
- [ ] One end connects to a curb node, the other to the sidewalk centerline

---

### How to Fix Issues

#### Moving Features

1. Select the feature (node or way)
2. Drag it to the correct location
3. If you accidentally move something else, press **Ctrl+Z** to undo

#### Adding Missing Tags

1. Select the feature
2. In the left panel, search for the correct preset (e.g., "Lowered Curb")
3. Alternatively, manually add tags in the expandable "Tags" table section

#### Connecting Features

If the editor shows a warning about disconnected features:

1. Select the feature
2. Click the warning message
3. Choose **Connect the features** to snap them together
4. Add tags (e.g., `highway=crossing`) as necessary

---

### Completing Validation

#### If Everything Looks Good

1. Save and upload any minor corrections you made
2. In the Tasking Manager panel on the right, answer **Yes** to "_Is this task well mapped?_"
3. Click **Submit task**

The task will turn from blue to green on the map to confirm that it has been validated.

#### If Issues Remain

1. Save and upload any corrections you made
2. In the Tasking Manager panel on the right, answer **No** to "_Is this task well mapped?_"
3. Add a **Comment** describing what needs fixing
4. Click **Submit task**

The task will return to the mapper for further work.

Done! **Thank you** so much for contributing to this project. Your contributions directly impact the lives of pedestrians in the area that use OpenStreetMap-based applications to safely navigate their environment.

---

### Tips for Validators

- **Use street-level imagery**: Enable Bing Streetside or Mapillary to verify curb types
- **Check connectivity**: Make sure features are connected and there are no gaps in the pedestrian network that don't exist on the ground
- **Be constructive**: Leave helpful comments when requesting changes
- **Focus on pedestrian features**: While you are free to fix other errors you find, prioritize crossings, curbs, and sidewalks

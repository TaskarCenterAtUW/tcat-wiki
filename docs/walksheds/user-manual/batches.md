---
title: Batches
nav_order: 8
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Batches

This section explains how to use the Batch tab to run multiple walkshed calculations from a single CSV file.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Overview

The **Batch** tab in the left toolbar allows you to run multiple walksheds in a single operation by uploading a CSV file. Each row in the CSV defines the parameters for one walkshed. The tool runs at most 3 walksheds concurrently, adds each result as a [Scenario](scenarios.md), and uploads them once at the end.

---

![Batch tab](../../resources/images/walksheds/user-manual/batches/batches-tab-light.png#only-light)
![Batch tab](../../resources/images/walksheds/user-manual/batches/batches-tab-dark.png#only-dark)

---

### CSV Format

Upload a CSV file with the following columns:

| Column              | Type    | Description                                                |
|:--------------------|:--------|:-----------------------------------------------------------|
| `lon`               | float   | Longitude of the origin point                              |
| `lat`               | float   | Latitude of the origin point                               |
| `maxuphill`         | float   | Maximum uphill slope (as a decimal, e.g. `0.08` for 8%)    |
| `maxdownhill`       | float   | Maximum downhill slope (as a decimal, e.g. `0.10` for 10%) |
| `avoidcurbs`        | boolean | Whether to avoid raised curbs (`true` or `false`)          |
| `reversewalkshed`   | boolean | Whether to compute a reverse walkshed (`true` or `false`)  |
| `maxcost`           | number  | Maximum travel cost budget (in seconds)                    |
| `name` _(optional)_ | string  | A label for the resulting scenario                         |

**Example CSV:**

```csv
lon,lat,maxuphill,maxdownhill,avoidcurbs,reversewalkshed,maxcost,name
-119.856092,47.233291,0.08,0.10,true,false,100,A
-119.856092,47.233291,0.07,0.03,false,false,300,B
-119.856092,47.233291,0.03,0.10,true,false,500,C
```

---

### Running a Batch

1. Select the **Batch** tab in the sidebar toolbar.
2. Select **Browse** to upload a CSV file.
3. Select **Run batch** to start processing.

A progress indicator at the bottom of the panel displays the number of completed walksheds, the percentage complete, and the number of saved scenarios. Select **Clear** to reset the batch panel.

---

Previous: [Datasets](datasets.md)

Next: [Sidewalk Score](sidewalk-score.md)

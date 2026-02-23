---
title: Services
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Services

This section explains how Points of Contact can create and manage data services linked to their project group.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._

---

### Overview

The **Services** page lists all services associated with the currently active project group. Use the **Search Service** field to filter by name, the **All** type dropdown to filter by service type, and the **Show Active** dropdown to toggle visibility of inactive services.

Each service entry displays its type badge (OSW, Flex, or Pathways), its name, and its **Id** (select the copy icon to copy it to your clipboard).

The options available on this page depend on your [roles](members.md#roles).

#### Member View

As a regular `member`, the Services page shows a read-only list of the project group's services with no edit controls.

![Services page member view](../../../resources/images/tdei-portal/user-manual/services/services-member-light.png#only-light)
![Services page member view](../../../resources/images/tdei-portal/user-manual/services/services-member-dark.png#only-dark)

#### Point of Contact View

As a **Point of Contact (`poc`)**, the Services page additionally shows a **Create Service** button (top right) and **Edit** / **Deactivate** controls on each service entry.

![Services page Point of Contact view](../../../resources/images/tdei-portal/user-manual/services/services-poc-light.png#only-light)
![Services page Point of Contact view](../../../resources/images/tdei-portal/user-manual/services/services-poc-dark.png#only-dark)

---

### Creating a Service

To create a new service, select **Create Service** (top right). This opens the **Create New Service** page.

![Create New Service page](../../../resources/images/tdei-portal/user-manual/services/create-service-light.png#only-light)
![Create New Service page](../../../resources/images/tdei-portal/user-manual/services/create-service-dark.png#only-dark)

Fill in the following fields:

| Field                  | Description                                                                                                                                    | Required |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| **Project Group Name** | Pre-filled with the current project group; read-only                                                                                           | —        |
| **Service Name**       | A name for the new service                                                                                                                     | Yes      |
| **Service Type**       | The type of data this service handles: `OSW`, `Flex`, or `Pathways`                                                                            | Yes      |
| **Service Boundaries** | A GeoJSON `FeatureCollection` defining the geographic boundary of this service. Use [geojson.io](https://geojson.io) to create a bounding box. | No       |

Select **Create** to create the service, or **Cancel** to return to the Services list without saving.

Once created, the new service will appear in the list.

![Services page after adding a service](../../../resources/images/tdei-portal/user-manual/services/services-poc-added-light.png#only-light)
![Services page after adding a service](../../../resources/images/tdei-portal/user-manual/services/services-poc-added-dark.png#only-dark)

---

### Editing or Deactivating a Service

From the Services page, in the Point of Contact (`poc`) view, each service entry has two controls:

- **Edit** — opens the service form to update the service name or boundaries
- **Deactivate** — opens a popup that allows for the deactivation of the service, removing it from the active list

---

Previous: [Project Groups](project-groups.md)

Next: [Members](members.md)

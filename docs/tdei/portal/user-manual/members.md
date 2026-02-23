---
title: Members
nav_order: 6
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Members

This section explains how Points of Contact can manage the members of their project group and assign roles.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._

---

### Overview

The **Members** section displays the members of the currently active project group. Access to this section depends on your role.

#### Member View

If you do not have the `poc` [role](#roles), navigating to Members will show a permission error: _"Oops! User doesn't have permission to access this page!"_

![Members page — permission denied](../../../resources/images/tdei-portal/user-manual/members/members-member-light.png#only-light)
![Members page — permission denied](../../../resources/images/tdei-portal/user-manual/members/members-member-dark.png#only-dark)

#### Point of Contact View

As a **Point of Contact (`poc`)**, the Members page shows a list of all members in the currently selected project group, with a **Search User** field to filter the list and an **Assign New User** button to add new members.

![Members page — Point of Contact view](../../../resources/images/tdei-portal/user-manual/members/members-poc-light.png#only-light)
![Members page — Point of Contact view](../../../resources/images/tdei-portal/user-manual/members/members-poc-dark.png#only-dark)

Each member entry displays:

| Column              | Description                                                |
|:--------------------|:-----------------------------------------------------------|
| **Name & Email Id** | The member's display name and registered email address     |
| **Contact Number**  | The member's phone number, if provided during registration |
| **Roles**           | The member's assigned roles                                |
| **Action** (⋮)      | Opens a menu with options to manage the member             |

---

![Assign Role to New User dialog — user not found error](../../../resources/images/tdei-portal/user-manual/members/user-not-found-light.png#only-light){ .img-right }
![Assign Role to New User dialog — user not found error](../../../resources/images/tdei-portal/user-manual/members/user-not-found-dark.png#only-dark){ .img-right }

### Assigning a New User

To add a new user to your project group:

1. Select **Assign New User** (top right)

2. In the **Assign Role to New User** dialog, enter the user's **Email Id**
    - The **Project Group ID** is pre-filled and read-only
    - If the email address is not registered with TDEI, an error banner will appear: _"The user '...' not registered with TDEI."_ The user must create a TDEI account before they can be added.

3. Under **Select Roles**, select one or more roles to assign to the user

4. Select **Assign** to confirm, or **Cancel** to dismiss

![Assign Role to New User dialog](../../../resources/images/tdei-portal/user-manual/members/assign-role-light.png#only-light)
![Assign Role to New User dialog](../../../resources/images/tdei-portal/user-manual/members/assign-role-dark.png#only-dark)

!!! danger "Assign roles carefully!"

    Accidentally assigning the wrong role (such as `poc`) to a user may enable them to make unwanted changes to the project group, member assignments, services, datasets, and more. **Make sure you are entering the correct Email Id and roles before selecting Assign**.

---

### Roles

| Role                        | Description                                                          |
|:----------------------------|:---------------------------------------------------------------------|
| **member**                  | A standard project group member with limited permissions             |
| **poc**                     | Responsible for the management of the project group                  |
| **osw_data_generator**      | OSW Data generator — can publish datasets for the project group      |
| **flex_data_generator**     | Flex Data generator — can publish datasets for the project group     |
| **pathways_data_generator** | Pathways Data generator — can publish datasets for the project group |

!!! note

    A user can hold multiple roles simultaneously. The `member` role is the default for all users added to a project group.

---

Previous: [Services](services.md)

Next: [Datasets](datasets.md)

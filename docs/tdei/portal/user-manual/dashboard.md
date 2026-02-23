---
title: Dashboard
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Dashboard

This section introduces the TDEI Portal dashboard, including the API key, project group selector, and account settings.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._

---

### Overview

After logging in, you will be taken to the **Dashboard**. The dashboard is the main landing page of the TDEI Portal and displays your current project group, your role within it, your Project Id, and your API key.

![TDEI Portal dashboard](../../../resources/images/tdei-portal/user-manual/dashboard/dashboard-light.png#only-light)
![TDEI Portal dashboard](../../../resources/images/tdei-portal/user-manual/dashboard/dashboard-dark.png#only-dark)

The dashboard shows:

| Field             | Description                                                                                     |
|:------------------|:------------------------------------------------------------------------------------------------|
| **Project Group** | The name of your currently active project group                                                 |
| **Roles**         | Your role(s) within the current project group (e.g., `member`)                                  |
| **Project Id**    | The unique identifier for your project group; select the copy icon to copy it to your clipboard |
| **My API Key**    | Your personal API key, used to authenticate programmatic access to TDEI data                    |

---

### API Key

Your **API key** is displayed on the dashboard in a masked field. Use the buttons next to it to manage it:

| Button      | Description                                         |
|:------------|:----------------------------------------------------|
| **Show**    | Reveals or hides your API key                       |
| **Copy**    | Copies the API key to your clipboard                |
| **Refresh** | Regenerates your API key, replacing the current one |

!!! warning

    Regenerating your API key will invalidate the previous key. Any applications or scripts using the old key will need to be updated.

---

### Project Group Selector

In the top-right of the header bar, the **Project Group** area (left of your username) displays your currently active project group. Select it to open the project group dropdown, which shows your current group and allows you to switch to another.

![Project group dropdown](../../../resources/images/tdei-portal/user-manual/dashboard/project-group-dropdown-light.png#only-light)
![Project group dropdown](../../../resources/images/tdei-portal/user-manual/dashboard/project-group-dropdown-dark.png#only-dark)

Switching project groups updates the other sections of the portal to reflect the selected group.

---

### User Menu

In the top-right of the header bar, select your **username** (right of the project group selector) to open the user menu, which provides the following options:

![User menu](../../../resources/images/tdei-portal/user-manual/dashboard/reset-password-option-light.png#only-light)
![User menu](../../../resources/images/tdei-portal/user-manual/dashboard/reset-password-option-dark.png#only-dark)

#### Reset Password

Select **Reset Password** to open a dialog where you can change your password by entering your current password and a new password.

![Reset password dialog](../../../resources/images/tdei-portal/user-manual/dashboard/reset-password-popup-light.png#only-light)
![Reset password dialog](../../../resources/images/tdei-portal/user-manual/dashboard/reset-password-popup-dark.png#only-dark)

!!! warning

    Upon successfully resetting your password, you will be logged out and will need to log in again with your new password.

#### Join With Referral Code

Select **Join With Referral Code** to join a project group using a referral code. Paste in the code shared with you and select **Apply**, or select **Cancel** to dismiss the popup.

![Join with referral code dialog](../../../resources/images/tdei-portal/user-manual/dashboard/join-with-referral-code-popup-light.png#only-light)
![Join with referral code dialog](../../../resources/images/tdei-portal/user-manual/dashboard/join-with-referral-code-popup-dark.png#only-dark)

#### Logout

Select **Logout** to sign out of the TDEI Portal and return to the [login screen](account-registration.md#logging-in).

---

Previous: [Account Registration](account-registration.md)

Next: [Project Groups](project-groups.md)

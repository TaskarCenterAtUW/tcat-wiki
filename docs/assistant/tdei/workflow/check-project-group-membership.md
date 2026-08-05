---
title: Check project-group membership
slug: check-project-group-membership
doc_type: workflow
questions:
    - How do I check whether a user belongs to a TDEI project group?
    - How do I verify a user's TDEI project group role?
audiences:
    - planner
    - jurisdiction
    - developer
products:
    - TDEI
topics:
    - tdei
    - project-groups
    - roles
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-05
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A user belongs to every TDEI project group because they belong to one project group.
        - A displayed project-group role grants permissions outside that role's documented scope.
related_pages:
    - tdei/portal/user-manual/project-groups.md
    - tdei/portal/user-manual/members.md
tags:
    - Assistant
---

<!-- @format -->

# Check project group membership

Use the [TDEI Portal](https://portal.tdei.us/) to verify whether a specific user belongs to the currently selected project group and to review the roles assigned to that user. You need access to the project group and must have the `poc` role to view and manage its member list.

## Short Answer

Switch to the relevant project group, open **Members**, and search for the user's account. The account is a member of that project group when it appears in the results with an assigned role.

## Significance

Project group membership controls which project resources a user can access. Checking the active group and the assigned role helps distinguish a missing membership from a permission or workspace configuration problem.

## What This Means

The **Members** page lists users in the active project group. A matching account with at least one displayed role confirms membership in that group. The result does not confirm membership in another group or establish that the user can perform every project action.

## What This Does Not Mean

- Finding a user in one group's member list does not show that they belong to other project groups.
- The existence of a user's email address or TDEI account in the system does not, by itself, confirm project-group membership.
- Membership does not automatically grant every dataset, service, workspace, or publishing permission. Review the displayed role and the relevant product workflow.

## How To Use This

1. Open the [TDEI Portal](https://portal.tdei.us/) and sign in.
2. Select the project group picker in the header or choose **Project Groups** in the left sidebar.
3. Search for the project group that you want to inspect, then select **Switch Project** for that group.
4. Select **Members** in the left sidebar.
5. Search for the user by the identifying information available in the member list.
6. Compare the result with the expected account and review the **Roles** shown for that user.

If **Members** is unavailable or displays a permission error, check whether the signed-in account has the required project group role.

If the user is not listed, verify the active project group and the user's registered account details.

## Example

A project administrator needs to confirm that a GIS analyst can access a group's data. The administrator switches to the correct project group, opens **Members**, searches for the analyst, and confirms the analyst's account and assigned role. The administrator then checks the relevant dataset or service permissions separately.

## Assistant Guidance

Ask the user to check and confirm that they have the correct project group selected. Do not ask the user to share any user details such as an email address. Do not infer that you can confirm membership of any specific account in any specific project group.

## Related Concepts

- [Project Groups](../../../tdei/portal/user-manual/project-groups.md)
- [Members](../../../tdei/portal/user-manual/members.md)

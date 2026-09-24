---
title: Workspace Review
nav_order: 15
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Workspace Review

This section explains how to open the workspace review map, filter review items, inspect changesets and notes, compare feature history, and discuss or resolve changes.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Open Workspace Review

1. **Open** a workspace from the [Dashboard](dashboard.md)
2. Open the workspace review view from the workspace actions
3. Review the map and the review panel

The review view shows the workspace name, a list of review items, and a map. When no changes match the current filters, the panel displays **No items to review**.

---

### Understand the review list

The review list can contain these item types:

- **Changeset** — a group of edits uploaded together. Each item can show its changeset number, review status, date, editor, comment, and counts of created, modified, and deleted elements.
- **Feedback** — feedback items appear in the list when **Feedback** is included in the review filters.
- **Note** — a workspace note with its note number, date, comment, and author.

Select an item to focus it on the map. The selected item is highlighted in the list, and its controls appear over the map.

The **Needs Review** label identifies changesets that have been flagged for review. Element-count badges show created, modified, and deleted elements in that order; they do not replace inspection of the individual edits.

---

### Configure review filters

1. **Select** the review settings button next to the workspace name
2. Choose the change categories to include:
    - **Changesets**
    - **Feedback**
    - **Notes**

3. Enable **Show Resolved** when you want resolved items included
4. Enable **Needs Review Only** when you want to limit the list to items requiring review
5. **Select** **Apply**

The review panel refreshes to reflect the filters you selected.

---

### Inspect a changeset

1. **Select** a changeset in the review list
2. Review the selected changeset's location and affected features on the map
3. Use **Edit Here** when you need to open the editing view for the selected area
4. Select the information button to open the changeset details
5. Select the discussion button to view or add discussion

The changeset details can include:

- **Comment**
- **Editor**
- **Source**
- **Imagery**
- **Hashtags**
- **Review Status**
- **Created By**
- **User ID**
- **Created At**
- **Closed At**

Use the source and imagery fields as review context, not as a substitute for project-specific evidence or local review procedures.

---

### Inspect feature history

When the selected changeset contains a feature that can be inspected, select it on the map. The history panel opens a diff viewer comparing the element's **Previous** and **Current** versions. It shows the element's version metadata, such as version, timestamp, changeset, and username, along with all of its tags. Review the tag differences alongside the geometry; a diff alone does not establish that the feature is correct.

---

### Add a discussion comment

1. **Select** the discussion button for a changeset
2. Review existing discussion entries
3. Enter a comment in **Start a discussion...**
4. **Submit** the comment with the send control

Use discussion to record questions, evidence requests, or decisions that other reviewers need to understand. Keep comments specific to the selected changeset or feature.

---

### Mark a changeset as reviewed

1. **Select** a changeset that needs review
2. Inspect its details, affected features, and discussion
3. Confirm that you have the role required to resolve changeset reviews
4. **Select** **Mark as Reviewed**

Only validators and owners can resolve changeset reviews. If the control is unavailable, ask a workspace owner or validator to complete the review action. Marking a changeset as reviewed records a review decision; it does not certify that all accessibility conditions are correct or publish the workspace automatically.

---

### Refresh the review list

1. **Select** the refresh button next to the workspace name
2. Review the updated item list

Use refresh when another contributor may have added or changed review items.

---

### Review an item

1. **Select** an item in the review list
2. Inspect its location and details on the map
3. Compare the edit with available imagery, field evidence, or project guidance
4. Follow your project's review process to resolve or escalate the item

Review does not prove that all accessibility conditions are correct and does not automatically grant approval or publication authority.

---

**Previous:** [Validate for a Project](projects/validate.md) | **Next:** [Export a Workspace](export.md)

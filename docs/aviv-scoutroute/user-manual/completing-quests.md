---
title: Completing Quests
nav_order: 4
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Completing Quests

This section explains how to view, select, answer, submit, and undo quests in AVIV ScoutRoute.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Viewing Available Quests

When you open a workspace, the map displays available quests as icons on the map. Each icon represents a data collection task for a specific feature. A quest is available when at least one applicable question is unanswered or when the element's last-edited time is at least the configured `recency_period` in the past.

The recency period controls visibility only. It does not expire, delete, or invalidate answers already saved on the element. When a quest becomes visible again, previously submitted answers are prefilled for review and revalidation.

Long Form Quest Definition schema version `3.2.1` allows `recency_period: 0`, which makes an answered quest immediately eligible for resurvey without a waiting period. Other workspace, quest-type, and map visibility settings still apply.

!!! tip

    Quest icons stack when you're zoomed out. **Zoom in** to see all available quests in a dense area.

---

### Selecting a Quest

1. Tap on a quest icon on the map

2. A panel appears, showing:
    - The feature type
    - Questions about that element
    - Descriptions or instructions
    - The answer options

3. The map highlights the feature the quest is asking about

![AVIV ScoutRoute quest panel with the sidewalk feature highlighted on the map](../../resources/images/aviv-scoutroute/user-manual/05-completing-quests/01-quest-element-highlight-light.avif#only-light){ .img-contained style="--img-width: 33%;" }
![AVIV ScoutRoute quest panel with the sidewalk feature highlighted on the map](../../resources/images/aviv-scoutroute/user-manual/05-completing-quests/01-quest-element-highlight-dark.avif#only-dark){ .img-contained style="--img-width: 33%;" }

To close a quest without answering:

- Tap the Close (++x++) icon in the upper right corner of the quest panel

---

### Answering a Quest

The way you answer depends on the quest type. Common input methods include:

| Input Type               | How to Answer                                                   |
| :----------------------- | :-------------------------------------------------------------- |
| **Single Choice**        | Tap one option; it will be highlighted with a pink border       |
| **Multiple Choice**      | Tap one or more options; selected items show pink borders       |
| **Numeric Entry**        | Use the on-screen keypad to enter a number                      |
| **Free-Form Text Entry** | Type your response (max 255 characters)                         |
| **Photo request**        | Use the camera control when the quest asks for a location photo |

For detailed information about each quest type, see [Quest Types](quest-types.md).

!!! note

    You can tap a selected option again to deselect it before submitting.

Answers that were submitted previously can appear prefilled when you reopen a quest. This is expected: the form uses the existing element data so you can review and revalidate it. A response selected during the current visit but not submitted is local form state and is discarded when you close the form.

If an earlier answer makes a follow-up question inapplicable, the follow-up is hidden and does not block completion. If you clear or deselect a previously saved response and submit, the corresponding data is deleted. Changing an earlier answer also removes outdated follow-up answers that no longer apply.

---

### Submitting a Quest

1. **Review your answer** - Double-check that your response is accurate

2. **Tap "Submit"** - Your answer is saved immediately to the workspace

3. **Quest disappears** - Fully completed quests are removed from the map

!!! success

    Once submitted, your contribution is committed to the workspace. It is available for the project's review workflow; it is not held in a separate changeset queue waiting for approval.

If another contributor changes the feature while you are answering, AVIV ScoutRoute opens **Resolve Conflicts** and has not submitted your answer yet. For each changed tag, choose whether to keep **Your answer** or the **Existing value**, then select **Confirm** to submit the selected values together. Select **Cancel** to stop resolving the conflict.

If the feature was deleted before the answer could be saved, the app displays an **Answer could not be saved** message with the reason. For example, the message may say **Element deleted**; ask the project contact how to proceed.

![AVIV ScoutRoute conflict resolution panel showing the contributor's answer and existing value](../../resources/images/aviv-scoutroute/user-manual/05-completing-quests/02-conflict-resolve-dark.avif){ .img-contained .img-inline style="--img-width: 25%;" } ![AVIV ScoutRoute message explaining that an answer could not be saved because the element was deleted](../../resources/images/aviv-scoutroute/user-manual/05-completing-quests/03-conflict-deleted-dark.avif){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

When you submit a previously answered quest again after the recency period, the app can save the confirmed answers in a new changeset and update the element's `timestampEdited` value. This prevents the same accurate data from being repeatedly requested during the recency period.

### Reviewing Submitted Answers

Workspace owners and validators can use the **Changeset Review** feature to inspect submitted changesets. When the workspace is configured to automatically flag changesets for review, flagged changesets receive distinct styling in the review view. A user with the workspace **validator** or **owner** role can select **Mark as Reviewed** after inspecting a flagged changeset; the changeset then returns to the normal styling.

Review is performed after the changeset is committed to the workspace. Reviewers can inspect the submitted changes and make follow-up edits, which are also committed through changesets.

---

### Tips for Accurate Data Collection

#### Observe in Person

For the most accurate data:

- **Be at the location** when answering quests about physical features
- **Look at the actual feature** rather than relying on map imagery alone
- **Take your time** to ensure accurate observations

#### When to Use "Unknown"

Some quests include an "Unknown" or "Can't determine" option. Use this when:

- You cannot physically access or see the feature
- The feature is obscured (construction, parked vehicles, etc.)
- You're unsure about which answer option is correct

!!! warning

    Submitting inaccurate data degrades the quality of the dataset. When in doubt, use "Unknown" or skip that question rather than guessing.

#### Handling Ambiguous Situations

If a feature doesn't clearly match any of the provided options:

1. Choose the **closest match** available
2. If there's a free-form text field, add clarifying notes
3. If truly ambiguous, consider using "Unknown" or skipping the quest

---

### Skipping Quests

You don't have to complete every quest you open! To skip a quest:

1. Tap the Close (++x++) icon in the upper right corner
2. The quest remains on the map for later (or for another user)

You can also hide individual quests you want to skip - refer to [Map Interface - Hide Quest](map-interface.md#hide-quest).

---

### Undoing Submitted Answers

Made a mistake? You can undo recent submissions:

1. Select the **Undo button** in the bottom left
2. Select the quest answer that you want to revert
3. Select **Undo**

For more detailed instructions, see [Undo Changes](map-interface.md#undo-changes).

---

### Group Quest Selection

The quest multi-select feature makes it easier to apply the same answers to multiple similar features at once, saving time when features share characteristics.

**How to use:**

1. Long-press on one of the quests
2. Tap each feature you want to include - selected features show a **purple checkmark**
3. Tap a selected feature again to deselect it
4. Tap **"Answer Quests"** to proceed
5. Answer the questions (your responses apply equally to all selected features)
6. Tap **Submit** when ready

**Example scenario:**

You're at an intersection where all eight curb ramps have the same characteristics. Instead of answering eight separate quests, you can:

1. Select all eight curb features
2. Answer the questions once
3. Submit - all eight quests are completed with the same data

!!! warning

    Only use group quest selection when you're confident that all selected features share the same characteristics. If features differ, answer them individually.

---

### Next Steps

- Review the different [Quest Types](quest-types.md) in detail
- Learn about [App Settings](app-settings.md) for managing quests and preferences

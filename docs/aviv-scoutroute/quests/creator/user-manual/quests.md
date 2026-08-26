---
title: Quests
nav_order: 5
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Quests

This section explains how to create and configure quest questions, answer choices, numeric validation, and dependencies.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._{ .guides-list-ref }

---

### Add a Quest

1. **Select** **Add Quest** under the element that should contain the question
2. **Enter** a numeric identifier in **Quest ID** and keep it distinct from the other quests in the definition
3. **Enter** the question in **Quest Title**
4. **Enter** instructions or context in **Description**
5. **Select** a value in **Quest Type**
6. **Enter** the answer tag in **Quest Tag** when the selected type requires one
7. **Enter** a URL in **Quest Image URL** only when the question needs an image

![Quest Definition Creator quest editor showing Quest ID, Quest Title, Description, Quest Type, Quest Tag, and Quest Image URL](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/01-quest-editor-light.avif#only-light)
![Quest Definition Creator quest editor showing Quest ID, Quest Title, Description, Quest Type, Quest Tag, and Quest Image URL](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/01-quest-editor-dark.avif#only-dark)

---

### Quest Fields

| Field               | Purpose                                                                                                   |
| :------------------ | :-------------------------------------------------------------------------------------------------------- |
| **Quest ID**        | Numeric identifier used to identify the question and reference it from dependencies                       |
| **Quest Title**     | Question shown to the contributor                                                                         |
| **Description**     | Supporting instructions or context                                                                        |
| **Quest Type**      | Determines the answer control used by AVIV ScoutRoute                                                     |
| **Quest Tag**       | Tag associated with the answer for the supported answer types                                             |
| **Quest Image URL** | Optional URL for an image shown with the question; the Creator displays PNG/JPEG size and dimension hints |

---

### Choose a Quest Type

The current Creator interface exposes these quest types:

| Quest type          | Use it for                                                   |
| :------------------ | :----------------------------------------------------------- |
| **ExclusiveChoice** | A question where the contributor selects one answer          |
| **MultipleChoice**  | A question where the contributor can select multiple answers |
| **Numeric**         | A measurement or count entered as a number                   |
| **TextEntry**       | A short free-form response                                   |

Choose the type before configuring type-specific fields. The Creator removes fields that do not apply to the selected type from the JSON Preview.

---

### Configure Answer Choices

**ExclusiveChoice** and **MultipleChoice** quests use answer choices.

1. **Select** **+ Add Choice**
2. **Enter** the stored answer in **Value**
3. **Enter** the contributor-facing label in **Choice Text**
4. **Enter** an optional image URL in **Image URL**
5. **Enable** **Enable optional picture-taking prompt** when that answer should offer a picture-taking step
6. **Use** **Move choice up**, **Move choice down**, or **Delete choice** to organize the choices

The **Value** and **Choice Text** fields are required. Keep the stored values stable because dependencies refer to them.

![Quest Definition Creator answer-choice editor showing Value, Choice Text, Image URL, and the optional picture-taking prompt](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/02-answer-choices-light.avif#only-light)
![Quest Definition Creator answer-choice editor showing Value, Choice Text, Image URL, and the optional picture-taking prompt](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/02-answer-choices-dark.avif#only-dark)

---

### Set Numeric Validation

For a **Numeric** quest, use **Numeric Validation** to limit accepted values:

1. **Select** **Numeric** from **Quest Type**
2. **Enable** **Enable minimum** when the answer needs a lower bound
3. **Enter** the lower bound in the number field that appears
4. **Enable** **Enable maximum** when the answer needs an upper bound
5. **Enter** the upper bound in the number field that appears
6. **Explain** the expected unit in **Quest Title** or **Description**

Check the range against the intended measurement and unit before exporting.

---

### Add a Dependency

A dependency displays a quest only when another quest in the same element has the required answer.

1. **Add** another quest to the same element before configuring the dependency
2. **Select** **Single** or **Multiple (AND)** under **Dependency**
3. For **Single**, **choose** the sibling quest in **Dependent Question**
4. **Choose** or enter the matching answer in **Required Value**
5. For **Multiple (AND)**, **add** each condition and verify that all conditions must be satisfied
6. **Review** the dependency in the JSON Preview and Validation panel

Select **None** when the quest should not depend on another question. Use the stored **Value** from the dependent choice, not its display label, when defining a choice dependency.

![Quest Definition Creator dependency editor showing Single dependency mode, Dependent Question, and Required Value](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/03-dependency-editor-light.avif#only-light)
![Quest Definition Creator dependency editor showing Single dependency mode, Dependent Question, and Required Value](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/quests/03-dependency-editor-dark.avif#only-dark)

---

### Reorder or Remove Quests

- **Select** **Move quest up** or **Move quest down** to change the order of questions within an element
- **Select** **Delete quest** to remove a question
- **Select** the quest heading to collapse or expand its fields

After changing a quest ID or order, review any dependencies that reference it.

---

### Next Steps

Continue to [Presets and Custom Icons](presets-and-icons.md) for optional reusable configuration, or go to [Validation and Export](validation-and-export.md) when the definition is complete.

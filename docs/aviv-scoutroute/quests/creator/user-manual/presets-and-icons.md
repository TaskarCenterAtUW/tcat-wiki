---
title: Presets and Custom Icons
nav_order: 6
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Presets and Custom Icons

This section explains how to use Feature Presets, Element Presets, Quest Presets, and custom icons in a quest definition. These preset types serve different purposes:

- **Feature Presets** define the point features that contributors can create in AVIV ScoutRoute.
- **Element Presets** help authors add common elements to a quest definition in the Creator.
- **Quest Presets** help authors add common quests to an element in the Creator.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._{ .guides-list-ref }

---

### Add a Feature Preset

A **Feature Preset** defines a predefined point feature that contributors can create from AVIV ScoutRoute. It supplies a name, an icon, and one or more tags. This is a configuration for the field-collection app, not a shortcut for adding content to the definition in the Creator.

1. **Select** **Add Feature Preset** in the **Feature Presets** panel
2. **Enter** the feature name in **Name**
3. **Select** **Pick Icon** and choose a feature-preset icon
4. **Enter** a tag key and value in the **Tags** fields
5. **Select** **Add Tag** to add additional tag pairs when needed
6. **Review** the generated tags and icon in the JSON Preview

Use **Move preset up**, **Move preset down**, and **Remove preset** to organize the list. Configure only point features that the field workflow needs.

![Quest Definition Creator Feature Presets panel showing a preset name, icon, and tag key/value fields](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/presets-and-icons/01-feature-presets-light.avif#only-light)
![Quest Definition Creator Feature Presets panel showing a preset name, icon, and tag key/value fields](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/presets-and-icons/01-feature-presets-dark.avif#only-dark)

---

### Enable Custom Icons

Custom icons are separate from question images and answer-choice images. They can identify a quest or a feature preset when a built-in icon is not sufficient.

1. **Select** **Enable Custom Icons** in the **Custom Icons** panel
2. **Select** **Add Custom Icon**
3. **Enter** a unique name in **Name**
4. **Enter** an absolute `http` or `https` URL in **URL**
5. **Select** **Quest** or **Feature preset** in **Context**
6. **Review** the preview and reference status

The current interface displays these custom-icon hints: SVG, less than `0.5 MB`, square, and approximately `96 px x 96 px`. Use a stable URL and resolve any URL, name, or icon-reference validation issue before exporting.

![Quest Definition Creator Custom Icons panel showing the name, URL, Context, and icon preview fields](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/presets-and-icons/02-custom-icons-light.avif#only-light)
![Quest Definition Creator Custom Icons panel showing the name, URL, Context, and icon preview fields](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/presets-and-icons/02-custom-icons-dark.avif#only-dark)

---

### Match an Icon to Its Context

Use a custom icon only in the context selected for that entry:

- A **Quest** custom icon can be selected as an element or quest icon
- A **Feature preset** custom icon can be selected for a feature preset

If the same graphic is needed in both contexts, create one custom-icon entry for each context and select the matching entry where it is used. A custom icon does not replace a **Quest Image URL** or an answer-choice **Image URL**.

---

### Use Element Presets

**Element Presets** help authors add common elements to the quest definition in the Creator. An element groups the quests for a mapped feature type and includes its element type, quest query, and element icon.

1. **Select** **Element Presets** in the element editor
2. **Choose** a matching element preset
3. **Review** the generated **Element Type**, **Quest Query**, and **Element Icon** values
4. **Adjust** the generated values when they do not match the intended workspace data
5. **Add** quests to the element or continue to [Use Quest Presets](#use-quest-presets)

Element Presets make it easier to add a common element structure to the definition. They do not define a feature that contributors can create in AVIV ScoutRoute; use a **Feature Preset** for that purpose.

If no matching element preset is available, enter the element values manually as described in [Elements](elements.md).

---

### Use Quest Presets

**Quest Presets** scaffold questions to help authors add common quests to an element in the Creator.

1. **Enter** or select the element type that should receive the preset
2. **Select** **Quest Presets** in the element's **Quests** section when a matching preset is available
3. **Choose** the preset to add its questions
4. **Review** every generated ID, title, description, type, tag, choice, and dependency

If the editor says that no quest presets are configured for the element type, add the quests manually by following [Quests](quests.md).

---

### Next Steps

Continue to [Validation and Export](validation-and-export.md) to check the completed optional sections and produce the JSON file.

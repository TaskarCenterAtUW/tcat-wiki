---
title: Getting Started
nav_order: 2
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Getting Started

This section explains how to open the Quest Definition Creator, start a definition, load an existing file, resume a draft, and choose a color theme.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._{ .guides-list-ref }

---

### Prerequisites

Before you begin, make sure you have:

- A web browser with access to the [Quest Definition Creator](https://taskarcenteratuw.github.io/asr-quests/)
- An existing Long Form Quest Definition JSON file to revise, or an idea of the type of data collection needed for your project
- A backup of any existing definition before loading or upgrading it

Refer to the [Long Form Quest Definition Guide](../../index.md) and [Element Query Guide](../../element-query.md) for additional information.

---

### Open the Creator

1. **Open** the [Quest Definition Creator](https://taskarcenteratuw.github.io/asr-quests/)
2. **Review** the welcome page and the Creator and schema versions shown in the footer after entering the editor

![Quest Definition Creator welcome page with Resume Current Draft, Create New Definition, and Choose File controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/getting-started/01-landing-page-light.avif#only-light)
![Quest Definition Creator welcome page with Resume Current Draft, Create New Definition, and Choose File controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/getting-started/01-landing-page-dark.avif#only-dark)

---

### Choose a Starting Point

Choose the option that matches your task:

| Welcome-page option       | Use it when                                                                                   |
| :------------------------ | :-------------------------------------------------------------------------------------------- |
| **Resume Current Draft**  | You want to continue a draft saved in this browser on this device                             |
| **Create New Definition** | You want to start with a blank definition using the Creator's latest-supported schema version |
| **Choose File...**        | You want to load an existing JSON definition                                                  |

---

#### Create a New Definition

1. **Select** **Create New Definition**
2. **Review** the layout of the empty editor, the default `recency_period` value, and the schema version in the JSON Preview
3. **Continue** to [Add Element](elements.md)

![Quest Definition Creator blank definition with Definition Settings, empty Elements panel, JSON Preview, and Export controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/getting-started/02-new-definition-light.avif#only-light)
![Quest Definition Creator blank definition with Definition Settings, empty Elements panel, JSON Preview, and Export controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/getting-started/02-new-definition-dark.avif#only-dark)

---

#### Load an Existing Definition

1. **Select** **Choose File...**
2. **Choose** a Long Form Quest Definition JSON file from the file picker
3. **Review** the loaded structure in the editor, the schema version in the footer, and the Validation panel
4. **Keep** the original file unchanged until you have reviewed and exported the edited definition

If the Creator identifies a compatible schema upgrade, follow the upgrade steps in [Validation and Export](validation-and-export.md#upgrade-a-compatible-definition).

---

#### Resume a Draft

The Creator autosaves edits in the browser's local storage. To continue a saved draft:

1. **Open** the Creator in the same browser and on the same device used to edit the draft
2. **Select** **Resume Current Draft** when it is available
3. **Review** the definition and validation status before continuing

A locally saved draft is not a shared or centrally stored copy. Export the definition when you need a backup or need to move it to another device.

---

### Choose a Color Theme

Use the theme controls in the header to select **light**, **dark**, or **auto**. The theme changes the Creator's appearance; it does not change the definition data.

---

### Next Steps

Continue to [Editor Overview](editor-overview.md) to learn how the Creator is organized, or go directly to [Elements](elements.md) to begin building a quest definition.

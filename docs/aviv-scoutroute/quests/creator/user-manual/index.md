---
title: Quest Definition Creator User Manual
nav_order: 1
tags:
    - User Manual
    - External
    - User
---

<!-- @format -->

## Quest Definition Creator User Manual

This user manual explains how to use the [Quest Definition Creator](https://taskarcenteratuw.github.io/asr-quests/) to create, edit, validate, and export AVIV ScoutRoute Long Form Quest Definition JSON files.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._{ .guides-list-ref }

---

### About the Quest Definition Creator

The Quest Definition Creator is a browser-based utility for building and maintaining the JSON files that define AVIV ScoutRoute quests. It can:

- Start a definition from a blank supported schema version
- Load an existing definition for editing
- Resume a draft saved in the same browser on the same device
- Add elements and quests manually or from available presets
- Configure answer choices, dependencies, numeric bounds, and icons
- Show validation feedback and a live JSON preview
- Download valid JSON or copy it to the clipboard

The footer displays the Creator version and the Long Form Quest Definition schema version supported by that release. Record those versions when documenting or troubleshooting version-specific behavior.

![Quest Definition Creator editor showing the Elements panel, a sidewalk definition, validation status, JSON preview, and export controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/index/01-creator-light.avif#only-light)
![Quest Definition Creator editor showing the Elements panel, a sidewalk definition, validation status, JSON preview, and export controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/index/01-creator-dark.avif#only-dark)

!!! note "Workspace configuration is separate!"

    Exporting a definition creates a JSON file or copies it to your clipboard. It does not update a workspace automatically. Apply and test the exported definition in the intended workspace separately.

---

### Quick Start

1. **Open** the [Quest Definition Creator](https://taskarcenteratuw.github.io/asr-quests/)
2. **Choose** **Create New Definition**, **Choose File...**, or **Resume Current Draft**
3. **Add** and configure the elements and quests in the editor
4. **Resolve** validation errors and review any warnings
5. **Inspect** the JSON Preview, then select **Download** or **Copy to Clipboard**

For a guided first use, start with [Getting Started](getting-started.md).

---

### Additional Resources

- [Long Form Quest Definition](../../index.md)
- [Element Query Guide](../../element-query.md)
- [AVIV ScoutRoute User Manual](../../../user-manual/index.md)
- [Long Form Quest Definition JSON Schema](https://github.com/TaskarCenterAtUW/asr-quests/blob/main/schema/schema.json)

---

### Table of Contents

Quest Definition Creator User Manual Table of Contents

#### [Getting Started](getting-started.md)

This section explains how to open the Quest Definition Creator, start a definition, load an existing file, resume a draft, and choose a color theme.

#### [Editor Overview](editor-overview.md)

This section introduces the Quest Definition Creator panels and explains the global definition settings.

#### [Elements](elements.md)

This section explains how to define the map features that quests target.

#### [Quests](quests.md)

This section explains how to create and configure quest questions, answer choices, numeric validation, and dependencies.

#### [Presets and Custom Icons](presets-and-icons.md)

This section explains how to use Feature Presets, Element Presets, Quest Presets, and custom icons in a quest definition. These preset types serve different purposes:

- **Feature Presets** define the point features that contributors can create in AVIV ScoutRoute.
- **Element Presets** help authors add common elements to a quest definition in the Creator.
- **Quest Presets** help authors add common quests to an element in the Creator.

#### [Validation and Export](validation-and-export.md)

This section explains how to resolve validation issues, review the JSON preview, upgrade compatible definitions, and export a file.

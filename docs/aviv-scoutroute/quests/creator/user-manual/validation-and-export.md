---
title: Validation and Export
nav_order: 7
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Validation and Export

This section explains how to resolve validation issues, review the JSON preview, upgrade compatible definitions, and export a file.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../guides-list/index.md)._{ .guides-list-ref }

---

### Read the Validation Panel

The **Validation** panel checks the current definition while you edit it.

1. **Review** the status after each major change
2. **Read** each listed path and message when the panel reports an issue
3. **Return** to the field named by the path and correct the value
4. **Confirm** that the panel reports the definition is current and valid

Validation errors block **Download** and **Copy to Clipboard**. Warnings do not block export, but review them before sharing the definition.

![Quest Definition Creator Validation panel showing a definition error and the message that export is blocked](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/validation-and-export/01-validation-light.avif#only-light)
![Quest Definition Creator Validation panel showing a definition error and the message that export is blocked](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/validation-and-export/01-validation-dark.avif#only-dark)

---

### Review the JSON Preview

The **JSON Preview** is a live, machine-readable representation of the definition that AVIV ScoutRoute reads.

1. **Check** the `version` and `recency_period` values
2. **Check** the element order, element types, icons, and queries
3. **Check** each quest ID, type, tag, choices, numeric validation, and dependency
4. **Check** optional `feature-presets` and `custom-icons` sections when you enabled them

Use the [Long Form Quest Definition](../../index.md) guide and the [JSON Schema](https://github.com/TaskarCenterAtUW/asr-quests/blob/main/schema/schema.json) when a field's structure is unclear.

---

### Upgrade a Compatible Definition

The Creator may offer an upgrade when a loaded definition uses an older schema version that the current release can upgrade.

1. **Keep** the original JSON file as a backup
2. **Load** the definition in the Creator
3. **Compare** the loaded version with the supported schema version shown in the footer
4. **Select** the upgrade control when the Creator identifies a compatible upgrade
5. **Review** the changed definition in the editor, Validation panel, and JSON Preview
6. **Export** the upgraded definition only after reviewing project-specific questions, dependencies, icons, and tags

Do not replace an unavailable upgrade operation by changing only the version string. An upgrade also does not update a workspace automatically.

---

### Export the Definition

1. **Enter** a filename ending in `.json` in **Filename**, or keep the default `quest-definition.json`
2. **Confirm** that the Validation panel reports no blocking errors
3. **Select** **Download** to save the JSON file
4. **Select** **Copy to Clipboard** when you need to paste the JSON into another tool
5. **Open** the downloaded or pasted JSON and review it before sharing or applying it

![Quest Definition Creator Export panel showing the Filename field and Download and Copy to Clipboard controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/validation-and-export/02-export-light.avif#only-light)
![Quest Definition Creator Export panel showing the Filename field and Download and Copy to Clipboard controls](../../../../resources/images/aviv-scoutroute/quests/creator/user-manual/validation-and-export/02-export-dark.avif#only-dark)

---

### Apply and Test the Exported Definition

Export is the end of the Creator workflow, not the deployment step.

1. **Update** the intended workspace configuration with the exported definition using your project's established process
2. **Reload** the configuration in the target application when required
3. **Test** the element queries, question types, choices, dependencies, images, and icons in AVIV ScoutRoute
4. **Record** the Creator version, schema version, definition version, and test result

For contributor-facing app behavior, refer to the [AVIV ScoutRoute User Manual](../../../user-manual/index.md).

---

### Next Steps

Return to the [Quest Definition Creator User Manual](index.md) or review the [Long Form Quest Definition](../../index.md) guide for the underlying JSON structure.

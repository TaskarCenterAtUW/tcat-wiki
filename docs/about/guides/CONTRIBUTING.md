---
title: Contributing
---

<!-- @format -->

# Contributing

This guide explains how to contribute to the TCAT Wiki.

Note that, while minor external contributions are welcome, this guide is primarily intended for use by TCAT/GS staff.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](index.md)._

---

## Full Installation and Setup (Windows 10/11)

This section of the guide explains how to set up a Windows environment for contributing to the TCAT Wiki.

### Legend

1. Keyboard shortcut to press | Action

    (`Shift`+`C`) | Copy

2. Command to enter into terminal

    [`someCommand --arguments \<path>`]

### Prerequisites

1. Install [Visual Studio Code](https://code.visualstudio.com/)

    1. Install [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) plugin
    2. Install [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) plugin
    3. Install [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

2. Install mkdocs-material

    1. In Powershell terminal:

        [`pip install mkdocs-material`]

3. Install plugins

    1. In PowerShell terminal:

        [`pip install mkdocs-git-revision-date-localized-plugin`]

    2. In PowerShell terminal:

        [`pip install mkdocs-git-committers-plugin-2`]

4. Install image processing dependencies

    1. In Powershell terminal:

        [`pip install "mkdocs-material[imaging]"`]

    2. Install [MSYS2](https://www.msys2.org/)

        1. In UCRT64 terminal:

            1. Install cairo:

                [`pacman -S mingw-w64-ucrt-x86_64-cairo`]

            2. Install pngquant:

                [`pacman -S mingw-w64-ucrt-x86_64-pngquant`]

        2. Add to PATH:

            `C:\msys64\ucrt64\bin`

### Setup

1. Using VS Code, clone `https://github.com/TaskarCenterAtUW/tcat-wiki`

## Editing Instructions

Refer to the documentation for [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and the [MkDocs User Guide](https://www.mkdocs.org/user-guide/).

### Screenshots

For creating screenshots with a consistent style, Firefox DevTools is to be used.

1. Open Firefox DevTools

    (`F12`)

2. Open Responsive Design View

    (`Ctrl`+`Shift`+`M`)

3. Add custom device profiles:

    1. Name: `[Screenshot] Web - Portrait`

        1. Size: `671`x`1196`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0`

    2. Name: `[Screenshot] Web - Landscape`

        1. Size: `1196`x`671`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0`

4. Resulting screenshots will fit exactly within the 2px outside border present in the following screenshot templates:

    1. [Screenshot (Landscape)](../../../resources/images/template/screenshot-landscape.png)
    2. [Screenshot (Portrait)](../../../resources/images/template/screenshot-portrait.png)

5. It is recommended to remove embedded metadata, such as with the use of [ExifToolGUI](https://exiftool.org/gui/).

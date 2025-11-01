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

### Images

Where possible, follow these guidelines for images:

1. Format: 24-bit `.png`

2. Resizing: Scale images using `{ width="123" }`:

    `![alt text](image.png){ width="300" }`

Refer to [Material for MkDocs: Images](https://squidfunk.github.io/mkdocs-material/reference/images/) and [Material for MkDocs: Attribute Lists](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/#attribute-lists) for more information.

#### Screenshots

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

    1. [Screenshot (Landscape)](../../resources/images/template/screenshot-landscape.png)

    2. [Screenshot (Portrait)](../../resources/images/template/screenshot-portrait.png)

5. It is recommended to remove all embedded metadata, such as with the use of [ExifToolGUI](https://exiftool.org/gui/).

#### Image Annotations

For creating image annotations with a consistent style, follow these guidelines.

1. Highlight box

    2. Use: Indicating an area of focus in an image.

    3. Style

        1. Padding: `2px` distance from highlighted selection

        2. Outline

            1. Width: `1px`

            2. Color: `#4B2E83` ("Husky "Purple")

        3. Fill

            1. Color: `#FFC700` ("Spirit Gold")

            2. Opacity: `0.25`

    4. Example:

        ![alt text](../../resources/images/tdei-portal/login-h-forgot-password.png){ loading=lazy }

    5. Naming convention: For images with highlights, append `-h-$highlightedFeature`

        1. Example: `login.png` → `login-h-forgot-password.png`

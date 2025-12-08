---
title: Contributing
tags:
    - Guide
    - Internal
    - Developer
---

<!-- @format -->

# Contributing

This guide explains how to contribute to the TCAT Wiki.

Note that, while minor external contributions are welcome, this guide is primarily intended for use by TCAT/GS staff.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](guides-list/index.md)._

---

## Getting Started (Windows 10/11)

This section of the guide explains how to set up a Windows environment for contributing to the TCAT Wiki for the first time.

### Legend

1. Keyboard shortcut to press | Action

    (`Shift`+`C`) | Copy

2. Command to enter into terminal

    [`someCommand --arguments \<path>`]

### Installation and Setup

1. Install [Visual Studio Code](https://code.visualstudio.com/)

    1. Install VS Code Extensions

        1. [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

        2. [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

        3. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

        4. [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

2. Clone the repository

    ```powershell
    git clone https://github.com/TaskarCenterAtUW/tcat-wiki
    cd tcat-wiki
    ```

3. Install [Python](https://www.python.org/downloads/)

4. Set up Python virtual environment

    1. Create the virtual environment

        ```powershell
        python -m venv .venv
        ```

    2. Activate the virtual environment

        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```

    3. Install dependencies

        ```powershell
        pip install -r requirements.txt
        ```

5. (Optional) Install image processing dependencies for image optimization

    Only needed if you plan to optimize or process images in the documentation.

    1. Install [MSYS2](https://www.msys2.org/)

        1. In UCRT64 terminal:

            1. Install cairo:

                ```powershell
                pacman -S mingw-w64-ucrt-x86_64-cairo
                ```

            2. Install pngquant:

                ```powershell
                pacman -S mingw-w64-ucrt-x86_64-pngquant
                ```

        2. Add to PATH:

            `C:\msys64\ucrt64\bin`

            (Restart your terminal or system for PATH changes to take effect)

## Editing Instructions

Refer to the documentation for [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and the [MkDocs User Guide](https://www.mkdocs.org/user-guide/).

### Guide Files

If you're creating a guide file that should not appear in the auto-generated guides lists (for example, a supplementary guide nested within a subfolder), add the following hidden flag to your frontmatter:

```yaml
---
title: Your Guide Title
tags:
    - Guide
# skip-in-guides-lists: true
---
```

The `# skip-in-guides-lists: true` comment is a YAML comment that won't appear on the built page but tells the `generate-guides-lists.ps1` script to exclude this file from the guides list generation.

If you're creating a topic index page that has no direct guides but should still appear in the main guides list (e.g., user manuals with nested subfolders), add the following flag to its frontmatter:

```yaml
---
title: User Manual
tags:
    - Guide
# include-in-guides-list: true
---
```

### Images

Where possible, follow these guidelines for images:

1. Format: 24-bit `.png`

2. Resizing: Scale images using `{ width="123" }`:

    ```markdown
    ![alt text](image.png){ width="300" }
    ```

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

    1. [Screenshot (Landscape)](resources/images/template/screenshot-landscape.png)

    2. [Screenshot (Portrait)](resources/images/template/screenshot-portrait.png)

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

        ![Screenshot of TDEI Portal Login page with "Forgot Password?" highlighted.](resources/images/tdei-portal/login-h-forgot-password.png){ loading=lazy }

    5. Naming convention: For images with highlights, append `-h-$highlightedFeature`

        1. Example: `login.png` → `login-h-forgot-password.png`

#### QR Codes

1. Create QR codes using [Project Nayuki's QR Code generator library](https://github.com/nayuki/QR-Code-generator).

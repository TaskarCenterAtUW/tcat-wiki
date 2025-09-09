---
title: Contributing
---

# Contributing

This guide explains how to contribute to the TCAT Wiki.

Note that, while external contributions are welcome, this guide is primarily intended for use by TCAT/GS staff.

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

2. Install mkdocs-material

   1. In Powershell terminal:

      [`pip install mkdocs-material`]

3. Install plugins

   1. In PowerShell terminal:

      [`pip install mkdocs-git-revision-date-localized-plugin`]

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

         [`C:\msys64\ucrt64\bin`]

### Setup

1. Using VS Code, clone [`https://github.com/TaskarCenterAtUW/tcat-wiki`]

## Editing Instructions

Refer to the documentation for [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and the [MkDocs User Guide](https://www.mkdocs.org/user-guide/).

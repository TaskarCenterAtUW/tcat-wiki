# TCAT Wiki

This repository contains the files used to create the [TCAT Wiki](https://taskarcenteratuw.github.io/tcat-wiki/).

Included below is the installation process required for setup.

# TCAT Wiki Setup Guide

## Legend

1. Keyboard shortcut to press | Action

    (`Shift`+`C`) | Copy

2. Command to enter into terminal

    [`someCommand --arguments \<path>`]

## Installation Instructions

1. Install VS Code ([Visual Studio Code](https://code.visualstudio.com/))

   1. Install YAML plugin ([YAML - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml))

2. Install mkdocs-material

   1. In Powershell terminal:

        [`pip install mkdocs-material`]

3. Install image processing dependencies

   1. In Powershell terminal:

        [`pip install "mkdocs-material[imaging]"`]

   2. Install MSYS2 ([MSYS2](https://www.msys2.org/))

      1. In UCRT64 terminal:
        
        1. Install cairo:

            [`pacman -S mingw-w64-ucrt-x86_64-cairo`]

        2. Install pngquant:

            [`pacman -S mingw-w64-ucrt-x86_64-pngquant`]

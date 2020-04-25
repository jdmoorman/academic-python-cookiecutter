# Cookiecutter Academic PyPackage

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Cookiecutter template for a Python package.

## About
`Cookiecutter` is a tool for generating templated projects.
This repository is a template for `cookiecutter` to generate a Python project.

## Quickstart
To use this template use the following commands and then follow the prompts from the terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:jdmoorman/cookiecutter-academic-pypackage`

This will create a directory with name `<project_slug>` in your current directory containing at least the following files, depending on which `bells_and_whistles` you select.

```bash
[project_slug]
├── src
│   └── [package_name]
│       ├── __init__.py
│       └── example.py
├── setup.py
├── setup.cfg
├── README.md
├── MANIFEST.in
└── LICENSE
```

## Credits

This template was forked from https://github.com/AllenCellModeling/cookiecutter-pypackage/ which was based on https://github.com/audreyr/cookiecutter-pypackage/

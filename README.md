# Cookiecutter Academic PyPackage

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Cookiecutter template for a Python package.

## About
`Cookiecutter` is a tool for generating templated projects.
This repository is a template for `cookiecutter` to generate a Python project. 
There are various optional features available through the template:
* You may use a different name for your github repository, PyPI distribution, and actual package.
* You may use a different description for github and PyPI.
* Optionally include a docs folder in the repository, compatible with [readthedocs.org](https://readthedocs.org/), to supplement `README.md`.
* Optionally use github actions to automatically publish to PyPI and run tests.
* Optionally use `pre-commit` with some sensible default commit hooks for linting.
* Optionally include a tests folder and `tox.ini` to for running test suites with `tox`.
* Optionally include `CODE_OF_CONDUCT.md` and `CONTRIBUTING.md`, if you welcome outside contributions.

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

After making some changes, you will be ready to publish your package.
* Put your code in the `src/[package_name]` directory. 
* Specify your dependencies in the currently empty `requirements = []` list in `setup.py`. 
* Try to install your project and check whether it is usable with
  ```bash
  $ pip install -e .
  $ python
  ```
  ```python
  >>> import package_name
  >>> package_name.__version__
  0.0.1
  >>> package_name.do_stuff()
  Expected output occurs, hopefully.
  ```
* Add usage and citation instrutions to `README.md`.


## Credits

This template was forked from https://github.com/AllenCellModeling/cookiecutter-pypackage/ which was based on https://github.com/audreyr/cookiecutter-pypackage/

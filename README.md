# Cookiecutter PyPackage

TODO: Update cookiecutter docs to reflect personal setup.
TODO: Make docs directory optional
TODO: Check compatibility with readthedocs.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Cookiecutter template for a Python package.

## About
`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a Python project which contains following:

* A directory structure for your project
* Prebuilt `setup.py` file to help you develop and install your package
* Includes examples of good Python practices, including tests
* Continuous integration
  * Preconfigured to generate project documentation
  * Preconfigured to automatically run tests every time you push to GitHub
  * Preconfigured to help you release your package publicly (PyPI)

We think that this template provides a good starting point for any Python project.

## Features
* Uses `tox` (an environment manager) and `pytest` for local testing, simply run `tox` 
from a terminal in the project home directory
* Runs tests on Windows, Mac, and Ubuntu on every branch and pull request commit using GitHub Actions
* Releases your Python Package to PyPI when you push to `stable` using GitHub Actions
* Automatically builds documentation using Sphinx on every push to master and deploys to GitHub Pages
* Includes example code samples for objects, tests, and bin scripts

## Example
* For an example of the base project that is built from this template, go to the
[example-build branch](https://github.com/AllenCellModeling/cookiecutter-pypackage/tree/example-build).

## Quickstart
To use this template use the following commands and then follow the prompts from the terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:jdmoorman/cookiecutter-pypackage`

**Original repo:** https://github.com/audreyr/cookiecutter-pypackage/

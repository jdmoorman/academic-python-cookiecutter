#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

test_requirements = [
    {% if cookiecutter.tests | lower == "true" -%}"pytest", "pytest-cov", "pytest-raises"{% endif %}
]

docs_requirements = [
    {% if cookiecutter.sphinx_docs | lower == "true" -%}"sphinx==1.8.5", "sphinx-rtd-theme"{% endif %}
]

setup_requirements = [
    {% if cookiecutter.tests | lower == "true" -%}"pytest-runner"{% endif %}
]

dev_requirements = [
    *test_requirements,
    *docs_requirements,
    *setup_requirements,
    {% if cookiecutter.precommit | lower == "true" -%}"pre-commit",{% endif %}
    "bump2version>=1.0.0",
    "ipython>=7.5.0",
    {% if cookiecutter.tests | lower == "true" -%}"tox>=3.5.2",{% endif %}
    "twine>=1.13.0",
    "wheel>=0.33.1",
]

requirements = []

extra_requirements = {
    "test": test_requirements,
    "docs": docs_requirements,
    "setup": setup_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *test_requirements,
        *docs_requirements,
        *setup_requirements,
        *dev_requirements,
    ],
}

{%- set license_classifiers = {
    "MIT": "License :: OSI Approved :: MIT License",
    "BSD": "License :: OSI Approved :: BSD License",
    "ISC": "License :: OSI Approved :: ISC License (ISCL)",
    "Apache Software License 2.0": "License :: OSI Approved :: Apache Software License",
    "GNU GPL v3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research ",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    description="{{ cookiecutter.pypi_short_description }}",
    entry_points={
        "console_scripts": [
            "my_example={{ cookiecutter.project_slug }}.bin.my_example:main"
        ],
    },
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="{{ cookiecutter.version }}",
    zip_safe=False,
)

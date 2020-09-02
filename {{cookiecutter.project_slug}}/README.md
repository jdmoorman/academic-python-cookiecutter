# {{ cookiecutter.project_name }}

[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.pypi_project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_project_name }}/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.pypi_project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_project_name }}/){% if cookiecutter.github_actions | lower == "true" %}
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/actions){% endif %}{% if cookiecutter.sphinx_docs | lower == "true" %}
[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.github_project_name }}/badge/?version=stable)](https://{{ cookiecutter.github_project_name }}.readthedocs.io/en/stable/?badge=stable) {% endif %}{% if cookiecutter.github_actions | lower == "true" %}
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}){% endif %}{% if cookiecutter.precommit | lower == "true" %}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black){% endif %}

{{ cookiecutter.github_short_description }}

---

## Installation

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```bash
$ pip install -U {{ cookiecutter.pypi_project_name }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent release.

If you don't have [pip](https://pip.pypa.io) installed, these [installation instructions](http://docs.python-guide.org/en/latest/starting/installation/) can guide
you through the process.

## Quick Start
```python
>>> from {{ cookiecutter.project_slug }} import Example
>>> a = Example()
>>> a.get_value()
10

```

## Citing
If you use our work in an academic setting, please cite our paper:

{% if cookiecutter.sphinx_docs | lower == "true" %}
## Documentation
TODO: readthedocs
For more information, read the docs.
{% endif %}

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

#### Suggested Git Branch Strategy
1. `master` is for the most up-to-date development, very rarely should you directly commit to this branch. Your day-to-day work should exist on branches separate from `master`. It is recommended to commit to development branches and make pull requests to master.
{%- if cookiecutter.github_actions | lower == "true" -%}
3. Even if it is just yourself working on the repository, make a pull request from your working branch to `master` so that you can ensure your commits don't break the development head. GitHub Actions will run on every push to any branch or any pull request from any branch to any other branch.
{%- endif -%}
4. It is recommended to use "Squash and Merge" commits when committing PR's. It makes each set of changes to `master`
atomic and as a side effect naturally encourages small well defined PR's.


#### Additional Optional Setup Steps:
* Create an initial release to test.PyPI and PyPI.
    * Follow [This PyPA tutorial](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives), starting from the "Generating distribution archives" section.

* Create a blank github repository (without a README or .gitignore) and push the code to it.
{% if cookiecutter.github_actions | lower == "true" %}
* Create an account on [codecov.io](https://codecov.io/) and link it with your GitHub account. Code coverage should be updated automatically when you commit to `master`.
* Add branch protections to `master`
    * Go to your [GitHub repository's settings and under the `Branches` tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/settings/branches), click `Add rule` and select the
    settings you believe best.
    * _Recommendations:_
      * _Require status checks to pass before merging_
{% endif %}{% if cookiecutter.sphinx_docs | lower == "true" %}
* Setup readthedocs. Create an account on [readthedocs.org](https://readthedocs.org/) and link it to your GitHub account.
    * Go to your account page and select "Import a Project".
    * Select the desired GitHub repository from the list, refreshing first if it is not present.
    * Go to the admin panel of the new project and make some changes to the "advanced settings":
        * Enable "Show version warning"
        * Enter "rtd-reqs.txt" into the "Requirements file" field
        * Enable "Install Project"
        * Enable "Use system packages"
        * Make sure to click save at the bottom when you are finished editing the settings
{% endif %}
* Delete these setup instructions from `README.md` when you are finished with them.

# {{ cookiecutter.project_name }}

[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.pypi_project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_project_name }}/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.pypi_project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.pypi_project_name }}/)
{% if cookiecutter.github_actions | lower == "true" -%}[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/actions){% endif %}
{% if cookiecutter.sphinx_docs | lower == "true" -%}[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest) {% endif -%}
{% if cookiecutter.github_actions | lower == "true" -%}[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}){% endif -%}
{% if cookiecutter.precommit | lower == "true" -%}[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black){% endif -%}


{{ cookiecutter.github_short_description }}

---

## Installation
**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}.git`

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


#### Additional Optional Setup Steps:
* Create an initial release to test.PyPI and PyPI.
  * Follow https://packaging.python.org/tutorials/packaging-projects/
* Make sure the github repository initialized correctly at
    * `https://github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}.git`
* Add branch protections to `master`
    * To protect from just anyone pushing to `master`
    * Go to your [GitHub repository's settings and under the `Branches` tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}/settings/branches), click `Add rule` and select the
    settings you believe best.
    * _Recommendations:_
      * _Require pull request reviews before merging_
      * _Require status checks to pass before merging_

#### Suggested Git Branch Strategy
1. `master` is for the most up-to-date development, very rarely should you directly commit to this branch. It is recommended to commit to development
branches and make pull requests to master.
3. Your day-to-day work should exist on branches separate from `master`. Even if it is just yourself working on the
repository, make a PR from your working branch to `master` so that you can ensure your commits don't break the
development head. GitHub Actions will run on every push to any branch or any pull request from any branch to any other
branch.
4. It is recommended to use "Squash and Merge" commits when committing PR's. It makes each set of changes to `master`
atomic and as a side effect naturally encourages small well defined PR's.

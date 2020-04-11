"""Top-level package for {{ cookiecutter.project_name }}."""

# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "{{ cookiecutter.version }}"

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"

__license__ = "{{ cookiecutter.open_source_license }}".rstrip(" license")
__copyright__ = "Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"


from .example import Example  # noqa: F401

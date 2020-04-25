class Example:
    """This class is only an example."""

    def get_value(self):
        """Spoiler: it's 10.

        Example:
            >>> from {{ cookiecutter.package_name }} import Example
            >>> e = Example()
            >>> e.get_value()
            10
        """
        return 10
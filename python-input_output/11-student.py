#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance."""
        if type(attrs) is list:
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of a Student instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

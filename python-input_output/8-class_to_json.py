#!/usr/bin/python3
"""Module that converts an object to a dictionary."""


def class_to_json(obj):
    """Return dictionary description of an object for JSON serialization."""
    return obj.__dict__

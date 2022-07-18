import importlib

from typing import List


def validate_by_function(location: str, lib_name: str):
    """Imports a validation function from a library"""

    # Process location to a path and the function that
    # needs to be extracted
    function_name = location.split(".")[-1]
    location = ".".join(location.split(".")[0:-1])
    valid_module = importlib.import_module(f"{lib_name}.validation.{location}")

    return valid_module.__dict__[function_name]


def validate_by_enum(value, enum: List, field: str):
    """Validates a field by an Enum"""

    if value not in enum:
        return False, {
            "loc": field,
            "message": f"Value of {value} is not supported. Please use one of the following {enum}",
        }

    else:
        return True, {}

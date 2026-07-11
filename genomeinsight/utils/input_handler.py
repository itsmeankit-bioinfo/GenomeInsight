"""
Input handling utilities for GenomeInsight.
"""

from pathlib import Path


def is_file(value: str) -> bool:
    """
    Return True if the supplied argument is an existing file.
    """
    return Path(value).is_file()


def input_type(value: str) -> str:
    """
    Determine whether the input is a sequence or a file.

    Returns
    -------
    str
        "file" or "sequence"
    """

    if is_file(value):
        return "file"

    return "sequence"
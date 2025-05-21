#!/usr/bin/env python3
"""The function should use a regex to replace occurrences of
certain field values."""
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:

    """filter_datum should be less than 5 lines long and use re.sub
    to perform the substitution with a single regex.

    Args:
        fields (list): List of field names to be redacted.
        redaction (str): The string to replace the field values with.
        message (str): The log line to be filtered.
        separator (str): The separator used in the log line.

    Returns:
        str: The filtered log line with the field values redacted.
    """

    pattern = r'({})=([^{}]*)'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

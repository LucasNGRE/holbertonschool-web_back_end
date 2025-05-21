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

"""Redacting Formatter class for filtering PII from log messages."""
import logging
from typing import List
from filtered_logger import filter_datum  # Assure-toi que filter_datum est dans ce fichier ou importé correctement


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that obfuscates specified fields in log messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the RedactingFormatter.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record by redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with redacted fields.
        """
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)
#!/usr/bin/env python3
"""
Module to hash passwords securely using bcrypt with salt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a generated salt using bcrypt
    and returns the hashed password as bytes.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

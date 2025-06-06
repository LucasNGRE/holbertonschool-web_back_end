#!/usr/bin/env python3
"""Module for basic authentication using Flask."""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication class that extends Auth."""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 encoded authorization header.

        Arguments:
        authorization_header -- the value of the Authorization header

        Returns:
        The Base64 encoded part of the header or None if not found
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

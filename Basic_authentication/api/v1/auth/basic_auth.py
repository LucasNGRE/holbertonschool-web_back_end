#!/usr/bin/env python3
"""Module for basic authentication using Flask."""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 encoded authorization header.

        Arguments:
        base64_authorization_header -- the Base64 encoded header

        Returns:
        The decoded string or None if decoding fails
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user credentials from the decoded Base64 authorization header.
        Arguments:
        decoded_base64_authorization_header -- the decoded Base64 header
        Returns:
        A tuple containing the username and password or (None, None) if extraction fails
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        try:
            user_info = decoded_base64_authorization_header.split(":")
            return user_info[0], user_info[1]
        except Exception:
            return None, None

#!/usr/bin/env python3
"""Module for basic authentication using Flask."""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session authentication class that extends the Auth class.
    """
    user_id_by_session_id = {}  # New class attribute

    def __init__(self):
        """Initialize SessionAuth."""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())  # Generate session ID like id in Base
        self.user_id_by_session_id[session_id] = user_id
        return session_id

#!/usr/bin/env python3
"""Module for basic authentication using Flask."""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ For the moment this class will be empty.
    It’s the first step for creating a new
    authentication mechanism"""
    def __init__(self):
        """Initialize theSessionAuth class."""
        super().__init__()
        # You can add any initialization code here if needed
        # For now, it just calls the parent class constructor
        pass

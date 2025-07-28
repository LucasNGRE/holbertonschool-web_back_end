#!/usr/bin/env python3
"""Module for Redis basic exercises.
"""
import redis # pyright: ignore[reportMissingImports]
import uuid
from typing import Union


class Cache:
    """Cache class for redis operations."""
    def __init__(self):
        """Store an instance of the redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        """Initialize BasicCache."""
        super().__init__()

    def put(self, key, item):
        """Assign the item value to self.cache_data[key]."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is not None:
            return self.cache_data.get(key)
        return None

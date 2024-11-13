#!/usr/bin/env python3
""" LIFO Cache replacement system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache module."""
    def __init__(self):
        """Initialize LIFOCache."""
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        return None

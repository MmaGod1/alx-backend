#!/usr/bin/env python3
""" LIFO Cache replacement system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache module."""
    def __init__(self):
        """Initialize LIFOCache."""
        super().__init__()
        self.order = []  # To keep track of insertion order

    def put(self, key, item):
        """Add item to cache with LIFO replacement if necessary."""
        if key is not None and item is not None:
            # Remove existing key if present to avoid duplicates
            if key in self.order:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        return None

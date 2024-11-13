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
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                recent_key = self.order.pop()
                del self.cache_data[recent_key]
                print(f"DISCARD: {recent_key}")

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        return None

#!/usr/bin/env python3
""" FIFO Cache replacement system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache module."""
    def __init__(self):
        """Initialize FIFOCache."""
        super().__init__()
        self.order = []  # To keep track of insertion order

    def put(self, key, item):
        """Add item to cache with FIFO replacement if necessary."""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        return None

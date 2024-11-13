#!/usr/bin/env python3
""" LRU cache replacement system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache module."""
    def __init__(self):
        """Initialize LRUCache."""
        super().__init__()
        self.order = []  # To keep track of insertion order

    def put(self, key, item):
        """Add item to cache with LRU replacement if necessary."""
        if key is not None and item is not None:
            """If key already exists,
            remove it from the order to update its position"""
            if key in self.cache_data:
                self.order.remove(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)  # Remove the first item in order
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is not None and key in self.cache_data:
            """ Move the accessed key to the end of the order list to
            mark it as recently used"""
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

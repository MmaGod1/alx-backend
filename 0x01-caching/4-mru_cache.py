#!/usr/bin/env python3
""" MRU Cache replacement system """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class """
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.order = []  # To track the most recently used order

    def put(self, key, item):
        """Add item to cache with MRU replacement if necessary."""
        if key is not None and item is not None:
            """ If key already exists, remove it from
            the order to update its position"""
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item in order (most recent)
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add item to cache and mark it as recently used
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve item from cache by key and update usage."""
        if key is not None and key in self.cache_data:
            """ Move the accessed key to the end of the order list
            to mark it as recently used."""
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

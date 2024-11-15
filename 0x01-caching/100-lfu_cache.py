#!/usr/bin/env python3
""" LFU Cache replacement system """
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFU Cache class """
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)  # Store frequency of each key
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add item to cache with LFU. """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the key with the lowest frequency
            min_freq = min(self.frequency.values())
            for k, f in list(self.frequency.items()):
                if f == min_freq and k in self.order:
                    discard_key = k
                    break
            self.order.pop(discard_key)
            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self.frequency[key] += 1  # Increment frequency
        self.order[key] = True  # Add to order to mark as most recently used

    def get(self, key):
        """ Retrieve item from cache and update its frequency and order. """
        if key is None or key not in self.cache_data:
            return None

        # Increase the frequency and update order to mark it as recently used
        self.frequency[key] += 1
        self.order.pop(key)
        self.order[key] = True
        return self.cache_data[key]

#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, do nothing.
        If self.cache_data exceeds MAX_ITEMS, discard
        the first added item (FIFO).
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
        If key is None or doesn't exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

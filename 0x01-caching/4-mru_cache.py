#!/usr/bin/env python3 
""" MRUCache module
"""
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    Implements a caching system that evicts the most recently used item.
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache
        Args:
            key (str): The key to add to the cache.
            item (Any): The item to be cached.

        If key or item is None, this method should not do anything.
        If the number of items exceeds MAX_ITEMS, the most recently used item is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent_key = self.order.pop()
            print(f"DISCARD: {most_recent_key}")
            del self.cache_data[most_recent_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item from the cache
        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value linked to the key or None if key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]

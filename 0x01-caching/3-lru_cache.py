#!/usr/bin/env python3
""" LRUCache module
This module defines the LRUCache class, which implements a Least Recently Used (LRU)
caching mechanism, inheriting from BaseCaching.
"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching.

    This class implements a caching system that follows the LRU (Least Recently Used)
    principle. When the cache exceeds a specified maximum number of items, it will
    discard the least recently used item.

    Attributes:
        cache_data (dict): A dictionary that holds the cached items.
        order (list): A list that tracks the order of keys based on usage 
                      for LRU eviction.
    """

    def __init__(self):
        """ Initialize the LRUCache.

        This method calls the parent class's initializer to set up the cache_data
        dictionary and any other necessary initialization from BaseCaching. It also
        initializes an order list to track the usage order of cached items.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache.

        This method adds an item to the cache with the given key. If the number of items
        exceeds the maximum allowed (MAX_ITEMS), the least recently used item will be
        discarded.

        Args:
            key (str): The key under which the item will be stored in the cache.
            item (any): The item to be cached.

        If key or item is None, this method will not perform any operation.
        If adding the item exceeds the cache limit, it will discard the least recently
        used item and print a message indicating which key was discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache.

        This method returns the value associated with the given key from the cache.
        It also updates the usage order since the item is being accessed.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists, or None if the key is None
            or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]

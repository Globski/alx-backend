#!/usr/bin/env python3
""" LIFOCache module
This module defines the LIFOCache class, which implements
a Last In, First Out (LIFO) caching mechanism, inheriting
from BaseCaching.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching.

    This class implements a caching system that follows
    the LIFO (Last In, First Out) principle.
    When the cache exceeds a specified maximum number of items, it will
    discard the last item added to the cache.

    Attributes:
        cache_data (dict): A dictionary that holds the cached items.
    """

    def __init__(self):
        """ Initialize the LIFOCache.

        This method calls the parent class's initializer
        to set up the cache_data dictionary and any other
        necessary initialization from BaseCaching.
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache.

        This method adds an item to the cache with the given key.
        If the number of items exceeds the maximum allowed (MAX_ITEMS),
        the last item added to the cache will be discarded.

        Args:
            key (str): The key under which the item will be stored in the cache.
            item (any): The item to be cached.

        If key or item is None, this method will not perform any operation.
        If adding the item exceeds the cache limit, it will discard the last added item
        and print a message indicating which key was discarded.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache.

        This method returns the value associated with the given key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists, or None if the key is None
            or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

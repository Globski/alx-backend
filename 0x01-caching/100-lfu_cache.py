#!/usr/bin/env python3
""" LFUCache module
This module defines the LFUCache class, which implements a Least Frequently 
Used (LFU) caching mechanism, inheriting from BaseCaching.
"""
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching.

    This class implements a caching system that follows the LFU (Least 
    Frequently Used) principle. When the cache exceeds a specified maximum 
    number of items, it will discard the least frequently used item, and 
    if there's a tie, it will use LRU (Least Recently Used) to decide 
    which item to evict.

    Attributes:
        cache_data (dict): A dictionary that holds the cached items.
        frequencies (dict): A dictionary that tracks the frequency of each 
                            key.
        order (dict): A dictionary that maps frequencies to a list of keys 
                      for LRU.
        min_freq (int): The minimum frequency of keys currently in the cache.
    """

    def __init__(self):
        """ Initialize the LFUCache.

        This method calls the parent class's initializer to set up the 
        cache_data dictionary and initializes the supporting data structures 
        for LFU management.
        """
        super().__init__()
        self.frequencies = {}
        self.order = {}
        self.min_freq = 0

    def put(self, key, item):
        """ Add an item to the cache.

        This method adds an item to the cache with the given key. If the 
        number of items exceeds the maximum allowed (MAX_ITEMS), the least 
        frequently used item will be discarded. In case of a tie, the least 
        recently used item will be discarded.

        Args:
            key (str): The key under which the item will be stored in the 
                        cache.
            item (any): The item to be cached.

        If key or item is None, this method will not perform any operation. 
        If adding the item exceeds the cache limit, it will discard the least 
        frequently used item and print a message indicating which key was 
        discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict()

        self.cache_data[key] = item
        self.frequencies[key] = 1
        self.min_freq = 1
        if self.min_freq not in self.order:
            self.order[self.min_freq] = []
        self.order[self.min_freq].append(key)

    def get(self, key):
        """ Retrieve an item from the cache.

        This method returns the value associated with the given key from the 
        cache. It also updates the frequency and usage order since the item 
        is being accessed.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists, or None if the 
            key is None or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """ Update the frequency of the given key. """
        freq = self.frequencies[key]
        self.frequencies[key] += 1
        new_freq = self.frequencies[key]

        self.order[freq].remove(key)
        if not self.order[freq]:
            if self.min_freq == freq:
                self.min_freq += 1
            del self.order[freq]

        if new_freq not in self.order:
            self.order[new_freq] = []
        self.order[new_freq].append(key)

    def _evict(self):
        """ Evict the least frequently used item from the cache. """
        key_to_evict = self.order[self.min_freq].pop(0)
        print(f"DISCARD: {key_to_evict}")
        del self.cache_data[key_to_evict]
        del self.frequencies[key_to_evict]

        if not self.order[self.min_freq]:
            del self.order[self.min_freq]

#!/usr/bin/env python3
"""
module for task 4
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    implements mru caching
    """

    def __init__(self):
        """
        initializes each instance
        """
        self.tracker = []
        super().__init__()

    def put(self, key, item):
        """
        adds a new data to the cache_data
        dictionary
        """
        i = 0

        if key is None or item is None:
            return

        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print("DISCARD: {}".format(self.tracker[-1]))
            del self.cache_data[self.tracker[-1]]
            self.tracker.pop(-1)

        if key in self.tracker:
            self.tracker.pop(self.tracker.index(key))
        self.tracker.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        gets data from the cache_data
        dictionary
        """
        if key is None:
            return None
        if key in self.tracker:
            self.tracker.pop(self.tracker.index(key))
            self.tracker.append(key)
        return self.cache_data.get(key, None)

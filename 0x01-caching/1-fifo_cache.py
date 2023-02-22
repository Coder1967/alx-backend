#!/usr/bin/env python3
"""
module for task 1
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    implements fifo caching
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
        if key is None or item is None:
            return
        if key in self.tracker:
            self.tracker.pop(self.tracker.index(key))
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_key = self.tracker[0]
            self.tracker.pop(0)
            del self.cache_data[item_key]
            print("DISCARD: {}".format(item_key))
        self.tracker.append(key)

    def get(self, key):
        """
        gets data from the cache_data
        dictionary
        """
        return self.cache_data.get(key, None)

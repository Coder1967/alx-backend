#!/usr/bin/env python3
"""
module for task 0
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic cache class
    """

    def put(self, key, item):
        """
        adds data into cache_data dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item


    def get(self, key):
        """
        gets data from the cache_data dictioinary
        """
        return self.cache_data.get(key)

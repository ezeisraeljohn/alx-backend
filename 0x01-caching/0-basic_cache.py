#!/usr/bin/env python3

""" This module implements Basic Caching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class implements the logic of the base class"""

    def put(self, key, item):
        """This adds to the caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the caching system"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

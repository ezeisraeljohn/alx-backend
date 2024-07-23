#!/usr/bin/env python3

""" This module implements Basic Caching """


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError("get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """This class implements the logic of the base class"""

    def put(self, key, item):
        """This adds to the caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the caching system dictionary"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

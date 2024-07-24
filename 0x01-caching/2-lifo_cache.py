#!/usr/bin/env python3

""" This module implements the FIFOCache class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """The LIFO class"""

    def put(self, key, item):
        """if cache is full, discard the last item in the cache

        Args:
            key (Any): The key of the item
            item (Any): The value
        """
        if not key and not item:
            pass

        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                return
            else:
                keys = self.cache_data.keys()
                discard_key = sorted(keys)[len(keys) - 1]
                del self.cache_data[discard_key]
                self.cache_data[key] = item
                print(f"DISCARD: {discard_key}")
                print()
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the caching system"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

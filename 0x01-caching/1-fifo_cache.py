#!/usr/bin/env python3

""" This module implements the FIFOCache class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The FIFO class"""

    def put(self, key, item):
        """_summary_

        Args:
            key (Any): The key of the item
            item (Any): The value
        """
        if not key and not item:
            pass

        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            discard_key = sorted(self.cache_data.keys())[0]
            del self.cache_data[discard_key]
            self.cache_data[key] = item
            print(f"DISCARD: {discard_key}")
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the caching system"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

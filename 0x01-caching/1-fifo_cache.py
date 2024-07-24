#!/usr/bin/env python3

""" This module implements the FIFOCache class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The FIFO class"""

    def put(self, key, item):
        if not key and not item:
            pass

        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            discard_key = sorted(self.cache_data.keys())[0]
            del self.cache_data[discard_key]
            print(f"DISCARDED {discard_key}")
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

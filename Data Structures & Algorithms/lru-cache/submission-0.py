from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # OrderedDict maintains insertion order, which we use to track recency.
        # The end of the dict represents the Most Recently Used (MRU) items.
        # The beginning (last=False) represents the Least Recently Used (LRU) items.
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        # Key missing? Return -1 per LRU Cache specifications.
        if key not in self.cache:
            return -1
        
        # Key found! Move it to the end to mark it as Most Recently Used.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key already exists, update its position to the end (MRU)
        # before updating its value.
        if key in self.cache:
            self.cache.move_to_end(key)
            
        # Insert or update the value.
        self.cache[key] = value

        # If we exceeded the allowed capacity, evict the LRU element.
        # popitem(last=False) removes and returns the first (oldest) (key, value) pair.
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
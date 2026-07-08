class Node:
    """
    Represents a single node in the doubly linked list.
    Stores the key-value pair and pointers to both adjacent nodes.
    """
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Hash map to provide O(1) lookups: maps key -> Node

        # Dummy nodes to eliminate edge cases (empty list handling)
        # left = Least Recently Used (LRU), right = Most Recently Used (MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        """Removes a given node from its current position in the linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        """Always inserts the given node at the rightmost position (MRU spot), right before the right dummy node."""
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Key exists: update its relevance by moving it to the MRU (right) side
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key already exists, remove the old node from the linked list
            self.remove(self.cache[key])
        
        # Create a new node and add/update it in the hash map and list (MRU position)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Eviction logic: if capacity is exceeded, remove the LRU node
        if len(self.cache) > self.cap:
            # The LRU node is always immediately to the right of the left dummy node
            lru = self.left.next
            self.remove(lru)          # Remove from linked list
            del self.cache[lru.key]   # Remove from hash map
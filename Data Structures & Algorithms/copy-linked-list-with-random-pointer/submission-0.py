"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # Dictionary to store the mapping from the original node to its deep copy.
        # This prevents infinite loops and ensures we don't duplicate nodes.
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Base Case: If the current node is null, there is nothing to copy.
        if head is None:
            # Note: This also correctly handles cases where head.random is None.
            return None
            
        # Memoization check: If we have already created a deep copy of this node 
        # during a previous recursive call, return that existing copy.
        if head in self.map:
            return self.map[head]

        # 1. Create a brand new node with the same value as the original node.
        copy = Node(head.val)
        
        # 2. Register the mapping immediately *before* making recursive calls.
        # This is critical for handling cycles (e.g., if a node's random pointer points back to itself).
        self.map[head] = copy
        
        # 3. Recursively copy the rest of the list and link it to the 'next' pointer.
        # This forces the creation of all subsequent nodes in the list lineally.
        copy.next = self.copyRandomList(head.next)
        
        # 4. Assign the random pointer. Because copyRandomList handles the full recursive 
        # traversal first, all nodes in the list are guaranteed to exist in self.map 
        # by the time the recursion unwinds to this point.
        copy.random = self.map.get(head.random)
        
        # Return the newly created deep copy of the current node.
        return copy
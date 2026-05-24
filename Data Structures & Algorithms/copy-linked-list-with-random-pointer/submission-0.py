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

        # you can use nonlocal in parent to achieve same thing, ask ai for details
        # since dictionaries are mutable, the keyword nonlocal is not necessary

        # Persistent "State" (The Hash Map)
        # This is the architectural reason. The algorithm requires a dictionary (self.map) to keep track of visited nodes across multiple recursive calls.
        # By defining self.map = {} inside __init__, that dictionary becomes tied directly to the object instance.
        # With a Class: The hash map lives cleanly on the object (self). The function can easily read and write to it across recursive cycles without messing up other instances of Solution.
        # Without a Class (Option 2): You are forced to pass the dictionary through every single recursive call function signature (memo_map=None), or resort to using risky global variables which can bleed data between separate tests.

        # If you see class Solution:, use self. (nonlocal will not work here to share data across separate class methods).

        # If you see a function inside a function (with no class layout), use nonlocal (or direct mutation). self has absolutely no meaning here and will cause an error because there is no object instance.

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Base Case: If the current node is null, there is nothing to copy.
        if head is None:
            # Note: This also correctly handles cases where head.random is None.
            return None
            
        # Memoization check: If we have already created a deep copy of this node 
        # during a previous recursive call, return that existing copy.
        # HERE IS THE CHECKING LINE!
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
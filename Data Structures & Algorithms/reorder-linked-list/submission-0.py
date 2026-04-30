# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Put all nodes into the deque
        queue = deque()
        curr = head.next # Start from second node because head stays at the front
        while curr:
            queue.append(curr)
            curr = curr.next
            
        # 2. Rebuild the list by alternating front and back
        curr = head
        while queue:
            # Pick from the back
            if queue:
                curr.next = queue.pop()
                curr = curr.next
            
            # Pick from the front
            if queue:
                curr.next = queue.popleft()
                curr = curr.next
        
        # 3. CRITICAL: Set the last node's next to None to avoid cycles
        curr.next = None
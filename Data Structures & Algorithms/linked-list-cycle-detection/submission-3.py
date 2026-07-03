# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the start of the list.
        # 'slow' moves 1 step at a time; 'fast' moves 2 steps at a time.
        slow, fast = head, head

        # Ensure 'fast' and 'fast.next' exist before moving.
        # If 'fast' reaches the end (None), there is no cycle.
        while fast and fast.next:
            slow = slow.next          # Move slow pointer forward by 1 node
            fast = fast.next.next     # Move fast pointer forward by 2 nodes
            
            # If there's a cycle, the fast pointer will eventually "lap" 
            # the slow pointer, and they will meet at the exact same node.
            if slow == fast:
                return True           # Cycle detected!
                
        # The fast pointer reached the end of the list, meaning it's a straight line.
        return False
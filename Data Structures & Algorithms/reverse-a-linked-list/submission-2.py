# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # --- 1. Base Case ---
        # If the list is empty, there is nothing to reverse.
        if not head:
            return None

        # --- 2. Initialize newHead ---
        # Assume this node is the new head of the reversed list.
        # If this is the last node, this assignment sticks and propagates back up.
        newHead = head
        
        # --- 3. Recursive Step ---
        # If there's a next node, we can dive deeper into the list.
        if head.next:
            # Recurse until we reach the very last node.
            # 'newHead' will capture that final node and pass it all the way back up.
            newHead = self.reverseList(head.next)
            
            # --- 4. The Pointer Flip ---
            # This is where the actual reversal happens as the recursion unwinds.
            # 'head.next' is the neighbor node. We make that neighbor's 'next' 
            # point back to the current 'head'. (e.g., 1 -> 2 becomes 1 <- 2)
            head.next.next = head
            
        # --- 5. Break the Old Link ---
        # Isolate the current node from its old forward connection.
        # This is crucial for the original first node (which becomes the new tail)
        # so it doesn't cause a cyclic loop pointing back to the second node.
        head.next = None

        # Return the new head of the reversed list (the original tail node)
        return newHead
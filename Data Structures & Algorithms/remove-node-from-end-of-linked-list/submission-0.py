class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        # This handles edge cases like removing the first node in the list.
        dummy = ListNode(0, head)
        
        # 'left' starts at the dummy (before the head)
        # 'right' starts at the actual head
        left = dummy
        right = head

        # Step 1: Advance the 'right' pointer 'n' steps forward.
        # This creates a "gap" of size 'n' between the two pointers.
        while n > 0:
            right = right.next
            n -= 1

        # Step 2: Move both pointers forward until 'right' hits the end (null).
        # Because of the gap, when 'right' is at the end, 
        # 'left' will be exactly one node BEFORE the node we want to delete.
        while right:
            left = left.next
            right = right.next

        # Step 3: Delete the node by skipping over it.
        # We point left's 'next' to the node after the target.
        left.next = left.next.next
        
        # Return the actual start of the list (skipping our dummy)
        return dummy.next
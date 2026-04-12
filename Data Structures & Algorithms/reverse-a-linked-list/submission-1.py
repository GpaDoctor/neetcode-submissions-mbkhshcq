# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # treat them like ppl
        prev = None
        # curr is at box1
        curr = head

        while curr:
            # curr write box1 treasure map on temp
            temp = curr.next
            
            # box1 terasure map change to point to prev
            curr.next = prev
            
            # prev now go to curr position which is box1
            prev = curr
            
            # curr follows the temp written treasure map and go to box2
            curr = temp 
        
        return prev

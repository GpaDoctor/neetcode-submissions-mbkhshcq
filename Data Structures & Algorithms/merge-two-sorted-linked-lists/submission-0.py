# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the node is also a ppl
        dummy = node = ListNode()

        # it is important to note that list2 and list2 are not list but pointers
        # here we treat them as 2 ppl, list1 and list2
        while list1 and list2:

            # list1 say his box1's value is smaller
            if list1.val < list2.val:

                # node draws his treasure map to point to list1's box1
                node.next = list1

                # list1 walks to his next box box2
                list1 = list1.next

            # now list2 say his box1's value is smaller
            else:
                
                # node draws his treasure map to point to list2's box1
                node.next = list2

                # list2 walks to his next box box2
                list2 = list2.next


            # node walks to his next box
            node = node.next
        
        # in the while condition when one list is done, the while loop breaks
        # in other words, one list must still remain 1 to some nodes
        # node writes the treasure map to point to either list1 or list 2
        node.next = list1 or list2

        # The Dummy (dummy) is a heavy post you hammered into the ground on the shore before you started. It never moves.
        return dummy.next

        # The Chain (.next) is what connects the shore-post to the first plank, and the first plank to the second, and so on.
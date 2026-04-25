# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if not p and not q:
            return True
        
        # recursion
        # 1. Check if both current nodes (p and q) exist and have the same value
        if p is not None and q is not None and p.val == q.val:
            
            # 2. Dive into the left side
            # We ask: "Is the entire left subtree of p identical to the left subtree of q?"
            left_side_match = self.isSameTree(p.left, q.left)
            
            # 3. Dive into the right side
            # We ask: "Is the entire right subtree of p identical to the right subtree of q?"
            right_side_match = self.isSameTree(p.right, q.right)
            
            # 4. Final Verdict for this branch
            # If BOTH sides matched, we return True to the "parent" call above us.
            return left_side_match and right_side_match

        else:
            return False
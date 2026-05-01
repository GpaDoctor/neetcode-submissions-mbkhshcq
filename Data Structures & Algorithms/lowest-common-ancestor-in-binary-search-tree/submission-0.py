# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # first of all a bst is given
        # it means that the tree is sorted

        if not root or not p or not q:
            return None
        
        # this means the lca is on the left side
        if (max(p.val, q.val) < root.val):
            # so we go to the root left child
            return self.lowestCommonAncestor(root.left, p, q)
        # this means the lca is on the right side
        elif (min(p.val, q.val) > root.val):
            # so we go the the root right child
            return self.lowestCommonAncestor(root.right, p, q)
        # this means the root is INBETWEEN p and q
        else:
            return root
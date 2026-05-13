# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to track the allowed range for each node
        def valid(node, left, right):
            # Base case: An empty tree (or leaf child) is technically a valid BST
            if not node:
                return True
            
            # Check if the current node's value violates the current boundaries
            # It must be strictly greater than 'left' and strictly less than 'right'
            if not (left < node.val < right):
                return False

            # Recursively check the subtrees:
            # 1. Left child: Must be less than the current node's value (new upper bound)
            # 2. Right child: Must be greater than the current node's value (new lower bound)
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # For the root, the allowed range is (-∞, +∞)
        # Start the recursion with the root and the widest possible range (-infinity to +infinity)
        return valid(root, float("-inf"), float("inf"))
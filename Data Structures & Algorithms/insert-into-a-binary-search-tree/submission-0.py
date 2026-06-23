# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base Case: If we reach an empty spot, create and return the new node
        if not root:
            return TreeNode(val)

        # If the value to insert is greater than the current node's value,
        # go to the right subtree.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # If the value to insert is smaller, go to the left subtree.
        else:
            root.left = self.insertIntoBST(root.left, val)

        # Return the (now updated) root node back up the call stack
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: The target key is not in the tree (or the tree is empty)
        if not root:
            return root

        # Step 1: Navigate the tree to find the node to delete
        if key > root.val:
            # Target is larger, so look in the right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # Target is smaller, so look in the left subtree
            root.left = self.deleteNode(root.left, key)
        
        # Step 2: Found the target node! Handle the three deletion scenarios
        else:
            # Case 2a: Node has 0 or 1 child (No left child)
            # If there's no left child, we can just return the right subtree to take its place
            if not root.left:
                return root.right
            
            # Case 2b: Node has 1 child (No right child)
            # If there's no right child, return the left subtree to take its place
            elif not root.right:
                return root.left

            # Case 2c: Node has 2 children
            # We need to find the "Inorder Successor" (the smallest value in the right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left
            
            # Copy the successor's value to the current node
            root.val = cur.val
            
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize the counter with k and a placeholder for the result
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            # Base case: if the current node is None, return back up the call stack
            if not node:
                return

            # Step 1: Traverse the left subtree.
            # In a BST, the smallest elements are always to the far left.
            dfs(node.left)
            
            # Optimization check: If a previous recursive call already found 
            # the k-th element (cnt == 0), stop processing further.
            if cnt == 0:
                return
            
            # Step 2: Process the current node ("Visit").
            # Decrement the counter since we just visited a valid node in sorted order.
            cnt -= 1
            
            # If the counter hits 0, this current node is the k-th smallest.
            if cnt == 0:
                res = node.val  # Capture the value
                return          # Exit early
            
            # Step 3: Traverse the right subtree.
            # Only explored if we still haven't found the k-th smallest element.
            dfs(node.right)

        # Start the in-order DFS traversal from the root
        dfs(root)
        
        # Return the captured k-th smallest value
        return res
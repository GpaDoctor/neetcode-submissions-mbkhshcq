class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            # Base Case: If we hit an empty spot (None), it contributes 0 good nodes
            if not node:
                return 0

            # --- STEP 1: EVALUATE THE CURRENT NODE ---
            # 'res' acts as our local counter for this specific node.
            # If the current node's value is >= the highest value on the path from root,
            # it is a "good" node, so we start our count at 1. Otherwise, 0.
            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            
            # --- STEP 2: UPDATE THE PATH MAXIMUM ---
            # Before moving to children, we determine the new "highest value seen so far."
            # This ensures children know the maximum value they need to beat.

            # We update maxVal ONLY for this current path.
            maxVal = max(maxVal, node.val)
            
            # --- STEP 3: ACCUMULATE FROM SUBTREES ---
            # We now turn 'res' into a running total for the entire subtree.
            # We move down the LEFT branch; it returns the count of good nodes found there.

            # CRITICAL POINT: When we call dfs on the left, it gets a copy of maxVal. 
            # If the left side finds a huge number (like 100), it updates its own 
            # local maxVal, but it DOES NOT change the maxVal of the right side.
            
            # This branch only cares about its ancestors, not its siblings.
            res += dfs(node.left, maxVal)
            
            # We move down the RIGHT branch and add those results to our total.
            # When we start the right branch, we use the original maxVal
            # from THIS node, completely ignoring whatever happened on the left.
            res += dfs(node.right, maxVal)
            
            # --- STEP 4: BUBBLE UP ---
            # Return the total sum (Self + Left Results + Right Results) 
            # to whichever parent node called this function.
            return res

        # Kick off the recursion starting at the root.
        # The root is always a "good" node, so we pass its own value as the initial max.
        return dfs(root, root.val)
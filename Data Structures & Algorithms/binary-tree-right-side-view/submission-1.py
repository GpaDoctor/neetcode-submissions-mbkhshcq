class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # Use a queue for Level Order Traversal (BFS)
        # We start by putting the root in the queue
        q = deque([root])

        while q:
            # rightSide will keep track of the most recent node seen at this level
            rightSide = None
            # qLen captures how many nodes are in the CURRENT level
            qLen = len(q)

            # why need a variable qlen
            # since q is constantly updated in the for loop
            # it is important to have a constant for the for loop

            # Process all nodes belonging to the current level
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # Every non-null node becomes the new 'rightSide' value.
                    # Since we process level nodes from left to right, 
                    # the LAST node assigned here will be the rightmost one.
                    rightSide = node
                    
                    # Add children to the queue for the NEXT level
                    q.append(node.left)
                    q.append(node.right)
                    # the q append does not affect the for loop constant
            
            # After finishing the for-loop, if we found any valid nodes at this level,
            # rightSide currently holds the very last (rightmost) one.
            if rightSide:
                res.append(rightSide.val)
                
        return res

# ### Comparison for your revision:
# * **DFS Approach:** Relies on the **order of recursion** (Right then Left) and checking the `depth` against the `len(res)`.
# * **BFS Approach:** Relies on the **level-by-level queue** structure. You capture the last node processed in each level "batch".

# In the interactive visualization, you can see how the `rightSide` variable gets "overwritten" as you move across a level, eventually settling on the rightmost node before the level finishes.
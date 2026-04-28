# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# why dfs and not bfs
# You are right that sameTree runs from top to bottom. But because isSubtree calls itself on the left child first, it exhausts the entire left "bloodline" of the tree before it ever checks the right-side siblings.

# Think of it like exploring a cave:

# BFS: You walk 10 feet into every tunnel to see what's there, then 20 feet.

# DFS (Your Code): You pick the leftmost tunnel and walk until you hit a wall, then you come back and try the next one.

class Solution:   

    # The Search Logic (isSubtree)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # acts like a "scout" walking through the big tree.
        # The Logic: "Check right here! 
        # Does the tree starting at this current node look exactly like the subRoot?"
        # (This triggers the Verify Phase).
        if self.sameTree(root, subRoot):
            return True

        # The Logic: "If it didn't match at the current node, 
        # go look in the left branch OR look in the right branch." 
        # This keeps the search moving downward.
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))


    # checks if two nodes (and their children) are identical twins.
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # If we ran off the bottom of both trees at the same time 
    # and found nothing, that’s a perfect match!"
        if not root and not subRoot:
            return True

        # The Logic: "To keep going, both nodes must exist, 
        # and their numbers must be exactly the same."
        if root and subRoot and root.val == subRoot.val:
        
            # The Logic: "Don't stop yet! For it to be a total match, 
            # the left children must match AND the right children must match.
            # " Note the use of and here—if even one tiny leaf is different, 
            # the whole thing is a False.
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        return False
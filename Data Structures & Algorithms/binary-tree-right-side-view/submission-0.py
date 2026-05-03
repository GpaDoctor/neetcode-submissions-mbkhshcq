# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # it is important to note that in a binary search tree
        # there will always only be left and right child

        # res stores the rightmost node value for each level
        res = []


        def dfs(node, depth):
            # Base Case: If we reach a null child, stop recursion
            if not node:
                return None
            # Key Logic: If the current depth equals the size of our result list,   
            # it means this is the FIRST time we have visited this level.
            # Because we visit right children first, the first node seen 
            # at any new depth is guaranteed to be the rightmost one.
            if depth == len(res):
                res.append(node.val)

            # travels to the bottom right
            # Important: Visit the RIGHT child first to ensure it's the 
            # one that populates the 'res' list for the current depth.
            dfs(node.right, depth + 1)

            # Then visit the LEFT child. If it reaches a depth that was 
            # already filled by a right-side node, the depth == len(res) 
            # check will fail, and this node will be ignored.
            dfs(node.left, depth + 1)
        
        # Start the recursion from the root at depth 0
        dfs(root, 0)
        return res

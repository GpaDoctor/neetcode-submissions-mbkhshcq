# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is to store the ans
        res = []

        def dfs(node, depth):
            # define base case
            if not node: 
                return None
            
            # this means i just went down a level or lower in depth
            if len(res) == depth:
                res.append([])

            # i am currently the same depth as the tree
            # i can start to append same level
            res[depth].append(node.val)

            # bianry trees only have left and right child
            # enter the left one until the base case
            dfs(node.left, depth + 1)

            # we finished the left dfs
            # now lets do the right
            dfs(node.right, depth + 1)
            

        
        # i pass the root and the depth level into the function
        dfs(root, 0)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # base case
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            # logic short cut
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # if else
            # if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            #     balanced = True
            # else:
            #     balanced = False


            # Even if the scout finds out the tree is unbalanced,
            # they still have to tell their boss how tall the tree is at their level 
            # so the boss can do their own math.
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        
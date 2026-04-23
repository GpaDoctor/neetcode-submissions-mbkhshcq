# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            # this just means adjust the closest outer function variable
            # many developers use a list or an object, because modifying the contents of a list doesn't count as "re-assigning" the variable
            # When you use self.res, that value stays on the object after the function finishes.
            # nonlocal is "cleaner" because it's temporary; it exists only while the function is running and vanishes afterward.
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            # this is just for tracking purpose
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
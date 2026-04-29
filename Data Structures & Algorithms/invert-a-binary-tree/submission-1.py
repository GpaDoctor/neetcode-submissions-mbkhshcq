# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # python double linked list way
        # To answer your question directly: What is inside the queue is a reference to a TreeNode object.
        # It is not just the number (val), and it is not a "copy" of the node. 
        # It is a memory address pointing to the actual instance of the TreeNode class.
        queue = deque([root])
        # what does this save?
        # this saves a class type object aka oop 
        # aka a reference (or pointer) to that specific instance of the TreeNode class.
        # inside a double linked list

        while queue:
            # assgin the node to the class type object
            node = queue.popleft()

            # swap
            node.left, node.right = node.right, node.left

            # if node.left or node.right exists
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root



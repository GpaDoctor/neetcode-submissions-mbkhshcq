# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # --- Base Case ---
        # If either list is empty, it means we've reached an empty subtree (a null child)
        if not preorder or not inorder:
            return None

        # --- Step 1: Identify the Root ---
        # In Preorder (Root -> Left -> Right), the first element is always the current root.
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # --- Step 2: Locate the Root in the Inorder Array ---
        # In Inorder (Left -> Root -> Right), finding the root's position tells us 
        # exactly how many elements belong to the left vs. right subtrees.
        # 'mid' also perfectly represents the COUNT of elements in the left subtree.
        mid = inorder.index(root_val)
        
        # --- Step 3: Recursively Build the Left Subtree ---
        # preorder[1 : mid + 1]: 
        # Skip the root (index 0), and grab the next 'mid' elements for the left side.
        # inorder[:mid]: 
        # Everything from the start up to (but excluding) the root at 'mid'.
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # --- Step 4: Recursively Build the Right Subtree ---
        # preorder[mid + 1 :]: 
        # Everything after the root and the left subtree elements.
        # inorder[mid + 1 :]: 
        # Everything to the right of the root node in the inorder sequence.
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        # --- Step 5: Return the reconstructed tree node ---
        return root
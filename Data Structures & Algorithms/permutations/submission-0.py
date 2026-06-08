from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # --- BASE CASE ---
        # If the input list is empty, there is only one way to arrange it: 
        # an empty list. We return a list containing that empty list.
        if len(nums) == 0:
            return [[]]

        # --- RECURSIVE STEP ---
        # Slice the list to remove the first element (nums[0]) and recursively 
        # find all permutations of the remaining elements (nums[1:]).
        perms = self.permute(nums[1:])
        res = []
        
        # --- COMBINATION STEP ---
        # Take the element we held out (nums[0]) and insert it into every 
        # possible position of every permutation generated from the subproblem.
        for p in perms:
            # The number of available insertion slots is always len(p) + 1
            # (e.g., if p has 2 elements, we can insert at indices 0, 1, or 2)
            for i in range(len(p) + 1):
                # Create a shallow copy of the permutation to avoid overwriting 
                # the same list across different insertion iterations
                p_copy = p.copy()
                
                # Insert the held-out element at the current index
                p_copy.insert(i, nums[0])
                
                # Add the newly created permutation to our final results list
                res.append(p_copy)
                
        return res
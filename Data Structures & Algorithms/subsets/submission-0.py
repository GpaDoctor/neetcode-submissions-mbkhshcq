class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []     # This will store all the final subsets
        subset = []  # This is the "current" subset we are building

        def dfs(i):
            # Base Case: If the index 'i' reaches the end of nums, 
            # we've made a decision for every element.
            if i >= len(nums):
                # We append a COPY of subset because lists are mutable;
                # otherwise, future changes would overwrite this entry.
                res.append(subset.copy())
                return

            # --- DECISION 1: Include nums[i] ---
            # Add the current element to our path
            subset.append(nums[i])
            # Move to the next index with the element included
            dfs(i + 1)

            # --- DECISION 2: Exclude nums[i] ---
            # Backtrack: remove the element we just added to try the other path
            subset.pop()
            # Move to the next index without the element
            dfs(i + 1)

        # Start the recursion at the first index
        dfs(0)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # BASE CASE 1: Successful match
            # If the current sum equals our target, we've found a valid combination.
            if total == target:
                # We append a copy because 'cur' is modified in-place during backtracking.
                res.append(cur.copy())
                return
            
            # BASE CASE 2: Stop conditions (Pruning)
            # 1. i >= len(nums): We've run out of numbers to pick from.
            # 2. total > target: Current sum exceeded target (no point in continuing).
            if i >= len(nums) or total > target:
                return

            # --- DECISION 1: Include nums[i] ---
            # We add the number at the current index to our potential combination.
            cur.append(nums[i])
            # We stay at index 'i' for the next call because the problem allows 
            # using the same number an unlimited number of times.
            dfs(i, cur, total + nums[i])
            
            # --- BACKTRACK ---
            # Before moving to the next decision, we must remove the number we 
            # just added to "clean up" the state for the next branch of the tree.
            cur.pop()

            # --- DECISION 2: Exclude nums[i] ---
            # We move to index 'i + 1' to explore combinations that definitely 
            # do NOT include the current nums[i] anymore.
            dfs(i + 1, cur, total)

        # Start the recursion from index 0, with an empty list and a sum of 0.
        dfs(0, [], 0)
        return res
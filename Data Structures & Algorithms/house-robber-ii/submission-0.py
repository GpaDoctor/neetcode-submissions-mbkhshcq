from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case: If there's only one house, we must rob it to maximize loot.
        if len(nums) == 1:
            return nums[0]

        # memo[i][flag] stores the max profit from house 'i' onwards.
        # flag (0 or 1) tracks whether the very first house (index 0) was robbed.
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            # Base cases for recursion:
            # 1. Out of bounds (i >= len(nums)) -> no more houses to rob.
            # 2. If the first house was robbed (flag == True), we cannot rob the last house (i == len(nums) - 1).
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
                
            # Return cached result if this state has already been computed.
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            # Decision making at house 'i':
            # Option 1: Skip house 'i', move to house 'i + 1'. The 'flag' remains unchanged.
            skip_house = dfs(i + 1, flag)
            
            # Option 2: Rob house 'i', add its value, and move to house 'i + 2' (cannot rob adjacent).
            # If we are currently at the very first house (i == 0), we set the 'flag' to True.
            rob_house = nums[i] + dfs(i + 2, flag or (i == 0))
            
            # Store the best decision in the memo table and return it.
            memo[i][flag] = max(skip_house, rob_house)
            return memo[i][flag]

        # The result is the maximum profit between two choices:
        # 1. Start at house 0 (which sets the 'flag' to True initially).
        # 2. Start at house 1 (where the first house is skipped, so 'flag' is False).
        return max(dfs(0, True), dfs(1, False))
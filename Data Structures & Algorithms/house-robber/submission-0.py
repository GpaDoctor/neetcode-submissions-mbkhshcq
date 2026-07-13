class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize a memoization array with -1 to store calculated results.
        # This prevents us from re-solving the same subproblems over and over.
        memo = [-1] * len(nums)

        def dfs(i):
            # Base Case: If we go past the last house, there is no more money to rob.
            if i >= len(nums):
                return 0
            
            # Lookahead: If we have already calculated the max profit starting 
            # from house 'i', return it immediately instead of recalculating.
            if memo[i] != -1:
                return memo[i]
            
            # Core Decision: Choose the best outcome between:
            # 1. Skipping house 'i' -> look at house 'i + 1'
            # 2. Robbing house 'i' -> get its cash and skip to house 'i + 2'
            # Save the maximum result into our memo array before returning it.
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        # Begin the recursion starting at the first house (index 0)
        return dfs(0)
        
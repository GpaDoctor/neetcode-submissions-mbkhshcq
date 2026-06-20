# from typing import List

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:

#         # Define a helper function for Depth-First Search (DFS) / Recursion
#         def dfs(i):
#             # Base Case: If we have stepped beyond the last step (reached the top),
#             # no more cost is incurred, so we return 0.
#             if i >= len(cost):
#                 return 0
            
#             # Recursive Step:
#             # The total cost to reach the top from step 'i' is the cost of step 'i' 
#             # plus the minimum cost of our two choices:
#             # 1. Take 1 step forward -> dfs(i + 1)
#             # 2. Take 2 steps forward -> dfs(i + 2)
#             return cost[i] + min(dfs(i + 1), dfs(i + 2))

#         # The problem allows us to start either at index 0 or index 1.
#         # We find the minimum cost of both starting options and return the best one.
#         return min(dfs(0), dfs(1))



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr = [0, 1]
        profit = 0
        maxP = 0


        while ptr[1] < len(prices):
            if prices[ptr[0]] < prices[ptr[1]]:
                profit = prices[ptr[1]] - prices[ptr[0]]
                maxP = max(maxP, profit)
            else:
                ptr[0] = ptr[1]
            ptr[1] += 1
        return maxP


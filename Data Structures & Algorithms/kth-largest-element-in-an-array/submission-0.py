class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        negateNums = [-values for values in nums]
        heapq.heapify(negateNums)
        ans = []
        for i in range(k-1):
            heapq.heappop(negateNums)
        ans.append(-negateNums[0])
        return ans[0]
        
        

        
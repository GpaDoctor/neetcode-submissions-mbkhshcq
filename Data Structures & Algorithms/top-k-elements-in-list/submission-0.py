import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h ={}
        ans = []

        for i, value in enumerate(nums):
            if value in h:
                h[value]+= 1
            else:
                h[value] =1

        hByValue =[(-value, key) for key, value in h.items()]
        heapq.heapify(hByValue)

        for i in range(k):
            ans.append(hByValue[0])
            heapq.heappop(hByValue)

        
        ar = [item[1] for item in ans]

        return ar
        
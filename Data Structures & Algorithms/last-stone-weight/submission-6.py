class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = 0
        b = 0
        negStones = [-i for i in stones]
        heapq.heapify(negStones)

        while len(negStones) > 1:
            a = heapq.heappop(negStones)
            b = heapq.heappop(negStones)
            # if a == b:
            #     q = 0
            # else:
            #     if a-b:
            #         x = -(a-b)
            heapq.heappush(negStones, a-b)
        if len(negStones) == 0:
            return 0
        else:
            return abs(negStones[0])



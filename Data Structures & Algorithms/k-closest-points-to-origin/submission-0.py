from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        ans = []
        ansi = []

        for values in points:
            h.append([sqrt(pow(values[0] - 0, 2) + pow(values[1] - 0, 2)), values])

        heapq.heapify(h)
   

        for i in range(k):
            ans.append(h[0][1])
            heapq.heappop(h)
        return(ans)


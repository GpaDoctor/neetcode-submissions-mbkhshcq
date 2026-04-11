class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr = [0, len(heights)-1]
        ans = 0

        while ptr[0] < ptr[1]:
            area = (ptr[1]-ptr[0]) * min(heights[ptr[0]], heights[ptr[1]])
            ans = max(ans,area)

            if heights[ptr[0]] < heights[ptr[1]]:
                ptr[0] += 1
            else:
                ptr[1] -= 1

        return ans
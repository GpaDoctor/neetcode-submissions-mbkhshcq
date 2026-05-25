from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        index = 0

        for color in range(3):
            while counter[color] > 0:
                nums[index] = color
                index += 1
                counter[color] -= 1
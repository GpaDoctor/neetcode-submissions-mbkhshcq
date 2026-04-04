class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
        i = 0

        while i < len(nums):
            complement  = target - nums[i]

            if complement in store:
                return [min(i, store[complement]), max(i, store[complement])]
            else:
                store[nums[i]] = i
                i += 1
        return [0, 0]


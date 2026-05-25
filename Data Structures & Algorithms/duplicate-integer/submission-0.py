class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)


        for key, value in d.items():

            if value > 1:
                return True
        
        return False
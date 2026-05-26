class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """

        d={}

        for i in range(len(nums)):
            if nums[i] in d:
              return True
            else:
                d.update({nums[i]:1})
        return False
                  


 


           
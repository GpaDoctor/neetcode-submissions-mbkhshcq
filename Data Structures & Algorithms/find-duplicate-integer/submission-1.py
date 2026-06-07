class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Treat the absolute value of the current number as an index.
            # We use -1 because the problem constraints (for this classic 
            # algorithm) usually assume numbers are in the range [1, n].
            idx = abs(num) - 1
            
            # If the value at this index is already negative, it means we 
            # have visited this number before, identifying it as the duplicate.
            if nums[idx] < 0:
                return abs(num)
            
            # Otherwise, mark the number at this index as visited by 
            # flipping its sign to negative.
            nums[idx] *= -1
            
        return -1
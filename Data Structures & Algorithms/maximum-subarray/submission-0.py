class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSub with the first element (handles arrays with all negative numbers)
        # Initialize curSum to 0 to track the running total of the current subarray
        maxSub, curSum = nums[0], 0
        
        for num in nums:
            # If the current running sum drops below 0, it will only decrease 
            # the value of any future subarray. We reset it to 0 to start fresh.
            if curSum < 0:
                curSum = 0
                
            # Add the current number to our running subarray sum
            curSum += num
            
            # Update the maximum subarray sum found so far if the current sum is larger
            maxSub = max(maxSub, curSum)
            
        return maxSub

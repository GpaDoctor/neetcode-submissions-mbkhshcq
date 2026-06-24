class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l: Left pointer of the sliding window
        # total: Tracks the current sum of elements inside the window
        l, total = 0, 0
        
        # Initialize the result with infinity; if it remains infinity, 
        # it means no valid subarray was found.
        res = float("inf")

        # Iterate through the array using 'r' as the right pointer of the window
        for r in range(len(nums)):
            # Expand the window by adding the current element to the total sum
            total += nums[r]
            
            # Shrink the window from the left as long as the current sum 
            # meets or exceeds the target
            while total >= target:
                # Update 'res' with the minimum length found so far
                # (r - l + 1) calculates the size of the current window
                res = min(r - l + 1, res)
                
                # Remove the leftmost element from the sum to try and find a smaller window
                total -= nums[l]
                
                # Move the left pointer forward
                l += 1

        # If 'res' was updated, return it; otherwise, return 0 as per requirements
        return 0 if res == float("inf") else res
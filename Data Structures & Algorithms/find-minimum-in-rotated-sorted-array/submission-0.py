from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize result with the first element as a baseline
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # SHORTCUT: If the current subarray is already fully sorted from l to r
            # (i.e., no rotation drop-off exists between them), then nums[l] 
            # is guaranteed to be the minimum of this entire section.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # Calculate the midpoint
            m = (l + r) // 2
            
            # Capture the midpoint value as a potential minimum candidate
            res = min(res, nums[m])
            
            # CONDITION 1: Left half is sorted (from l to m)
            # Example: [3, 4, 5, 6, 1, 2] -> m is at 5, l is at 3. (5 >= 3)
            if nums[m] >= nums[l]:
                # Since the left half is a normal climbing slope, the minimum 
                # cannot be inside it. The "rotation drop-off" must be to the right.
                # We pivot our search to the right half.
                l = m + 1
            
            # CONDITION 2: Right half is sorted (from m to r)
            # Example: [5, 6, 1, 2, 3, 4] -> m is at 1, l is at 5. (1 < 5)
            else:
                # If the left half wasn't sorted, the right half must be.
                # This means the sudden drop-off (and the absolute minimum) 
                # is located somewhere in the left half. We pivot our search left.
                r = m - 1
                
        return res
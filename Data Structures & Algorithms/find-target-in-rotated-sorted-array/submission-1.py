from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Find the pivot (the index of the minimum element).
        # Since the array is sorted but rotated, it consists of two sorted subarrays.
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            
            # If the middle element is greater than the rightmost element,
            # the pivot must be in the right half (we need to look past m).
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the middle element is less than or equal to the rightmost element,
            # meaning the right half is properly sorted, and the pivot is at m or to its left.
            # why r = m. Not r = m - 1.
            # we are looking for the min element
            # this is not typical binary search. we didn't compare mid to target
            # so mid has to be included 
            else:
                r = m 

        # After the loop, l == r, pointing exactly at the minimum element (pivot).
        pivot = l

        # Step 2: Define a standard binary search helper function.
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Step 3: Search for the target in the two sorted portions.
        
        # Try searching in the left sorted portion (from index 0 up to the pivot - 1)
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        # If not found in the left portion, search in the right sorted portion (from pivot to the end)
        return binary_search(pivot, len(nums) - 1)
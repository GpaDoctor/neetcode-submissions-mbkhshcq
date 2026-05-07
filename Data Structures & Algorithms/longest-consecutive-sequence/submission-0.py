class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        numSet = set(nums)
        longest = 0

        # check every num in numSet
        for num in numSet:
            # Check if 'num' is the start of a sequence.
            # If (num - 1) exists, 'num' is part of a sequence but not the beginning. we can skip.
            if (num - 1) not in numSet:
                # true means num is the start of a sequence
                # so we start from length = 1
                length = 1

                # Mission: Incrementally check for the next consecutive integers
                while (num + length) in numSet:
                    # if true, we add one to see the next
                    length += 1
                # Update the global maximum length found so far
                longest = max(length, longest)
            # after one cycle, we check next num
            
        return longest


        
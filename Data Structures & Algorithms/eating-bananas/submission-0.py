import math
from typing import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible speed is 1 banana per hour.
        # The maximum useful speed is the size of the largest pile (max(piles)),
        # because eating more than that doesn't save any extra hours on a single pile.
        l, r = 1, max(piles)

        # Initialize the result to the maximum possible required speed.
        res = r

        # Perform a binary search to find the minimum valid eating speed 'k'.
        while l <= r:
            # Calculate the midpoint speed to test.
            k = (l + r) // 2

            # Calculate the total hours needed to eat all piles at speed 'k'.
            totalTime = 0
            for p in piles:
                # For each pile, hours taken = ceiling(pile_size / speed).
                # float(p) ensures float division before ceiling.
                totalTime += math.ceil(float(p) / k)

            # If Koko can finish all bananas within 'h' hours at speed 'k':
            if totalTime <= h:
                res = k  # Record 'k' as a potential answer.
                r = (
                    k - 1
                )  # Try to find a smaller valid speed in the left half.

            # If it takes too long (totalTime > h), speed 'k' is too slow.
            else:
                l = (
                    k + 1
                )  # Increase the minimum speed by searching the right half.

        return res
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        count = Counter(s)
        
        # Step 2: Build a max-heap based on character frequencies.
        # Python's heapq is a min-heap by default, so we store negative counts 
        # to simulate a max-heap (e.g., a frequency of 3 becomes -3).
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        # 'prev' keeps track of the character we just used in the previous step
        # so we don't accidentally place it immediately next to itself.
        prev = None
        res = ""
        
        # Step 3: Reconstruct the string greedily
        while maxHeap or prev:
            # If we need to place a character (prev exists) but the heap is empty,
            # it means we have remaining duplicate characters but no other unique 
            # characters left to separate them. Thus, reorganization is impossible.
            if prev and not maxHeap:
                return ""

            # Pop the most frequent character currently available
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Decrement the count (closer to 0 since it's a negative number)

            # If there was a character held back from the *previous* turn,
            # it is now safe to push it back into the heap.
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # If the character we just used still has remaining occurrences,
            # hold it back so it cannot be chosen in the very next iteration.
            if cnt != 0:
                prev = [cnt, char]

        return res
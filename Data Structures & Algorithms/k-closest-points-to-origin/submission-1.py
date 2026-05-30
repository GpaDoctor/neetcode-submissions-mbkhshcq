import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a max-heap to store the 'k' closest points found so far.
        # Python's 'heapq' is a min-heap by default, so we store distances 
        # as negative values to simulate max-heap behavior.
        maxHeap = []
        
        for x, y in points:
            # Calculate the squared Euclidean distance: x^2 + y^2.
            # We skip the square root (sqrt) because if a^2 < b^2, then a < b.
            # The negative sign allows the largest distance to stay at the top.
            dist = -(x ** 2 + y ** 2)
            
            # Push the distance and coordinates onto the heap.
            # heapq orders elements by the first value in the list (dist).
            heapq.heappush(maxHeap, [dist, x, y])
            
            # If the heap size exceeds 'k', remove the element with the 
            # "largest" distance (the most negative value in our max-heap).
            # This ensures we only keep the 'k' smallest distances.
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # Extract the remaining 'k' points from the heap to return.
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            
        return res
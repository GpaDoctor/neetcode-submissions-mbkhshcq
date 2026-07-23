import heapq
from typing import List


class Solution:

  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    # Sort the trips based on their starting locations
    trips.sort(key=lambda t: t[1])

    # Min-heap to keep track of ongoing trips, storing pairs of [end_location, numPassengers]
    minHeap = []
    curPass = 0

    for numPass, start, end in trips:
      # Remove all trips from the heap that have already ended by the current trip's start time
      while minHeap and minHeap[0][0] <= start:
        curPass -= heapq.heappop(minHeap)[1]

      # Add the passengers of the current trip to the current passenger count
      curPass += numPass

      # If the current passenger count exceeds the vehicle's capacity, return False
      if curPass > capacity:
        return False

      # Push the current trip's end time and passenger count into the min-heap
      heapq.heappush(minHeap, [end, numPass])

    # If all trips can be completed without exceeding capacity, return True
    return True
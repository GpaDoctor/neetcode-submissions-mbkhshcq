import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 'available' stores tasks that have arrived and are waiting to be processed.
        # Elements are tuples: (processTime, index). 
        # Min-heap ensures we always pick the shortest process time (and smallest index if tied).
        available = []
        
        # 'pending' stores all tasks sorted primarily by their enqueue (arrival) time.
        # Elements are tuples: (enqueueTime, processTime, index).
        pending = []
        for i, (enqueueTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processTime, i))

        time = 0  # Tracks the current timeline of the CPU
        res = []  # Stores the final order of executed task indices
        
        # Continue loop as long as there are tasks waiting to arrive OR tasks ready to be processed
        while pending or available:
            
            # Step 1: Push all tasks that have already arrived by the 'current time' into the available heap
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processTime, i))

            # Step 2: If no tasks are currently available, it means the CPU is idle.
            # Fast-forward 'time' to the arrival time of the next available pending task.
            if not available:
                time = pending[0][0]
                continue  # Restart the loop to push this next task into 'available'

            # Step 3: CPU processes the best available task.
            # Min-heap automatically pops the one with the shortest processTime (or smallest index)
            processTime, i = heapq.heappop(available)
            
            # Advance the CPU clock by the duration of the processed task
            time += processTime
            
            # Record the index of the completed task
            res.append(i)

        return res
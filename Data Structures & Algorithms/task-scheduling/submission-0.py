from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        count = Counter(tasks)
        
        # Step 2: Use a Max-Heap to always execute the most frequent task first.
        # Since Python only has a Min-Heap by default, we store frequencies as negative numbers.
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        
        # Step 3: Use a queue to track tasks that are on "cool-down" (idle period).
        # It stores pairs of: [remaining_count, time_when_it_becomes_available]
        q = deque()  
        
        # Continue processing until all tasks are executed and no tasks are waiting in the cool-down queue
        while maxHeap or q:
            time += 1

            if not maxHeap:
                # Optimization: If the heap is empty, the CPU must sit idle.
                # Instead of incrementing time by 1 repeatedly, we fast-forward 
                # 'time' directly to when the next task in the queue becomes available.
                time = q[0][1]
            else:
                # Pop the task with the highest remaining frequency (most negative value)
                # Adding 1 effectively reduces its absolute frequency by 1 (e.g., -3 + 1 = -2)
                cnt = 1 + heapq.heappop(maxHeap)
                
                # If there are still instances of this task left to process, 
                # put it into the cool-down queue. It can only be processed again at (current time + n)
                if cnt:
                    q.append([cnt, time + n])
            
            # Step 4: Check if the task at the front of the cool-down queue has finished its idle period.
            # If its available time matches the current time, push it back into the Max-Heap.

            # By writing if q and ..., you are taking advantage of a feature called short-circuit evaluation:
            # Python evaluates the condition from left to right.
            # If q is empty, q evaluates to False.
            # Because it is an and statement, Python already knows the whole condition cannot possibly be true.
            # It stops reading immediately and skips the rest of the line. It never even attempts to look at q[0][1], saving your code from a crash.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
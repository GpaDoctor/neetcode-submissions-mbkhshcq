from typing import List
# ONLY CATCH UP, NO OVERTAKING

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's starting position with its speed: [(pos, speed), ...]
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars by their starting position in descending order (closest to target first).
        # We process from closest to farthest because a car ahead dictates the max speed 
        # of any trailing car that catches up to it.
        # this sorts by p
        # can use pair.sort(lamda x: x[0], reverse = True)
        pair.sort(reverse=True)
        
        # This stack will store the time it takes for the lead car of each fleet to reach the target.
        # this stack is ALL LEAD CARS   
        stack = []
        
        for p, s in pair:
            # Calculate the exact time it would take this car to reach the target 
            # if it were driving alone: (Remaining Distance / Speed)
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            
            # If the current car (stack[-1]) takes LESS or EQUAL time to reach the target 
            # than the car ahead of it (stack[-2]), it means this car will catch up 
            # to the car ahead before or exactly at the target line.
            # Since cars cannot pass each other, they merge into a single fleet.
            # We pop the current car because it joins the slower fleet ahead and adopts its time.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # only lead car matters, if a car cannot form a fleet, its data is useless
                stack.pop()
                
        # The remaining elements in the stack represent the distinct fleets, 
        # each tracked by the time it takes the lead car of that fleet to finish.
        return len(stack)
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Start our target 'goal' at the very last index of the array
        goal = len(nums) - 1

        # Walk backward through the array, starting from the second-to-last element
        for i in range(len(nums) - 2, -1, -1):
            # Check if the current position 'i' plus the max jump distance 'nums[i]' 
            # is enough to reach or pass our current 'goal'
            if i + nums[i] >= goal:
                # If we can reach the goal from here, this index becomes our new goal.
                # We now only care about finding a way to reach this closer position.
                goal = i
                
        # If we successfully shifted the goal all the way back to the start index (0),
        # it means there is a valid path from the beginning to the end.
        return goal == 0
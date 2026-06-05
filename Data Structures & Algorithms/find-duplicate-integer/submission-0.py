class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect that a cycle exists and find an intersection point.
        # We start both pointers at the very first index (index 0).
        slow, fast = 0, 0
        
        while True:
            # The tortoise moves 1 step: next index is the value at the current index.
            slow = nums[slow]
            # The hare moves 2 steps: jumps to the value, then to that value's value.
            fast = nums[nums[fast]]
            
            # If they meet, it proves a cycle exists. 
            # Note: This meeting point is NOT necessarily the duplicate number yet!
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (which is the duplicate number).
        # We keep 'slow' inside the cycle where it met 'fast'.
        # We place a new pointer 'slow2' back at the very beginning (index 0).
        slow2 = 0
        while True:
            # Both pointers now advance at the exact same speed (1 step at a time).
            slow = nums[slow]
            slow2 = nums[slow2]
            
            # The exact index where they collide is the entrance to the cycle.
            # This entrance is guaranteed to be the duplicate number.
            if slow == slow2:
                return slow
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with 0s. 
        # If no warmer day is found later, the value remains 0.
        res = [0] * len(temperatures)
        
        # The stack will store pairs: [temperature, index]
        # It is "monotonic" because we keep temperatures in decreasing order.
        stack = []  

        for i, t in enumerate(temperatures):
            # While the stack isn't empty AND the current temperature 't' 
            # is warmer than the temperature at the top of the stack:
            while stack and t > stack[-1][0]:
                # We found a warmer day for the item at the top of the stack.
                # Pop it to process it.
                stackT, stackInd = stack.pop()
                
                # The number of days to wait is the difference between 
                # the current index (i) and the day we just popped (stackInd).
                res[stackInd] = i - stackInd
            
            # Push the current day's temperature and index onto the stack.
            # This day will stay in the stack until we find a warmer temperature in the future.
            # IMPORTANT
            stack.append((t, i))
            
        return res
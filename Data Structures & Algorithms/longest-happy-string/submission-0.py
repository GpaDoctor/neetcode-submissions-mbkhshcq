class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Keep track of the remaining counts for 'a', 'b', and 'c' using their indices (0, 1, 2)
        count = [a, b, c]
        res = []

        # Helper function to find the character with the highest remaining count,
        # skipping the character that is currently blocked/repeated.
        def getMax(repeated):
            idx = -1
            maxCnt = 0
            for i in range(3):
                # Skip if this character is temporarily blocked, or if we ran out of it
                if i == repeated or count[i] == 0:
                    continue
                # Greedily pick the character with the maximum count left
                if maxCnt < count[i]:
                    maxCnt = count[i]
                    idx = i
            return idx

        # 'repeated' keeps track of which character index is blocked from being used next.
        # It is set to -1 when no character is blocked.
        repeated = -1
        
        while True:
            # Try to get the available character with the highest count
            maxChar = getMax(repeated)
            
            # If no valid character can be picked (either all are 0, or the only one left is blocked),
            # we are done building the string.
            if maxChar == -1:
                break
            
            # Convert the index (0, 1, 2) back to its character ('a', 'b', 'c') and append it
            res.append(chr(maxChar + ord('a')))
            count[maxChar] -= 1
            
            # Check the end of the string: if the last two characters are identical, 
            # we must block this character from being picked in the next iteration.
            if len(res) > 1 and res[-1] == res[-2]:
                repeated = maxChar
            else:
                # If the last two aren't identical, any available character can be used next.
                repeated = -1

        return ''.join(res)
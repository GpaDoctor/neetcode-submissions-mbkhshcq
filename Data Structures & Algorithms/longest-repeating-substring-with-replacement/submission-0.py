class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # Create a set of all unique characters in the string.
        # We will try making a long string for EACH unique character.
        charSet = set(s)

        # note that we have to loop through all char in the set
        for c in charSet:
            # count: how many times our "target" character 'c' appears in the current window
            # l: the left boundary of our sliding window
            count = l = 0
            
            # r: the right boundary of our sliding window (expands every iteration)
            for r in range(len(s)):
                # If the new character entering the window matches our target, increment count
                if s[r] == c:
                    # the count stands for number of char matching the target
                    count += 1

                # LOGIC CHECK: 
                # (r - l + 1) is the TOTAL number of characters in the window.
                # (r - l + 1) - count is the number of "OTHER" characters (the ones we must change).
                # If these "others" exceed our budget 'k', the window is invalid.
                while (r - l + 1) - count > k:
                    # If the character we are about to slide past (leave behind) was our target,
                    # we must decrement the count because it's no longer in the window.
                    if s[l] == c:
                        count -= 1
                    
                    # Shrink the window from the left to try and get back under budget
                    l += 1

                # After the while loop, we know the current window [l...r] is VALID.
                # Update our global maximum result if this window is the longest seen so far.
                res = max(res, r - l + 1)
                
        return res
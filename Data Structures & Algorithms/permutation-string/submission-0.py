class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, s2 cannot possibly contain a permutation of s1
        if len(s1) > len(s2):
            return False

        # Initialize frequency arrays for the 26 lowercase English letters
        s1Count, s2Count = [0] * 26, [0] * 26
        
        # Populate counts for s1 and the very first window of s2 (same length as s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many letter frequencies match initially across all 26 letters
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # 'l' tracks the left boundary of our sliding window
        l = 0
        
        # 'r' tracks the right boundary, sliding from the end of the initial window to the end of s2
        for r in range(len(s1), len(s2)):
            # If all 26 frequencies match, we found a permutation!
            if matches == 26:
                return True

            # --- PHASE 1: Add the new character at 'r' to the window ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            
            # Update 'matches' based on how this addition affected the frequency
            if s1Count[index] == s2Count[index]:
                matches += 1  # The counts became equal, so we gained a match

            # This is for when s2 is JUST larger than s1
            # anything after that does not matter, since the match is updated already, 
            # and is changed only when the counts are equal again
            # take the example of s1:aab s2:caaac
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1  # They were equal before, but now s2 has too many, so we lost a match

            # --- PHASE 2: Remove the old character at 'l' from the window ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            
            # Update 'matches' based on how this removal affected the frequency
            if s1Count[index] == s2Count[index]:
                matches += 1  # The counts became equal, so we gained a match

            # This is for when s2 is JUST smaller than s1 (by exactly 1)
            # Anything after that does not matter, since the match is updated already, 
            # and is changed only when the counts are equal again
            # take the example of s1:aab s2:aatyubax
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1  # They were equal before, but now s2 has too few, so we lost a match
            
            # Slide the left pointer forward to maintain the fixed window size
            l += 1
            
        # One final check for the very last window position after the loop ends
        return matches == 26
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        charIndex = {}
        maxLength = 0
        start = 0
        
        for index, char in enumerate(s):
            if (char in charIndex) and  charIndex[char] >= start:
            # if (char in charIndex) and index >= start:
                start = charIndex[char] + 1

            charIndex[char] = index


            currentLength = index - start + 1
            if currentLength > maxLength:
                maxLength = currentLength
        # This is wrong, because a max length might have appeared in the middle, if we were to calculate it at the end, we would have missed it
        # return len(s) - start 
        return maxLength


        
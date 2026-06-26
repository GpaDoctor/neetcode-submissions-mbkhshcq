class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: If the input list is empty, there is no common prefix
        if not strs:
            return ""
            
        # Iterate through each character index of the very first string
        for i in range(len(strs[0])):
            # Compare this character against the character at the same index 'i' in all other strings
            for s in strs:
                # Mismatch conditions:
                # 1. 'i == len(s)' means we've hit the end of a shorter string 's'
                # 2. 's[i] != strs[0][i]' means the characters don't match anymore
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the common prefix found so far (from index 0 up to i)
                    return s[:i]
        
        # If the loop finishes without a mismatch, the entire first string 
        # is the longest common prefix (e.g., if strs = ["flow", "flow", "flow"])
        return strs[0]
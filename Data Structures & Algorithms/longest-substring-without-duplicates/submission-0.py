class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if there are duplicates
            while s[r] in window:
                # remove the left most element, which is the duplicate
                window.remove(s[l])
                # moe the ptr to the left
                l += 1
            # update the window, add the right element to the window
            window.add(s[r])

            # update the max res
            res = max(res, r - l + 1)
        return res
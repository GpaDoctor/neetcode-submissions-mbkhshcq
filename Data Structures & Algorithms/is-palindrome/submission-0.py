class Solution:
    def isPalindrome(self, s: str) -> bool:
        si = "".join(char.lower() for char in s if char.isalnum())


        for i in range(len(si) // 2):
            ptr0 = si[i] 
            ptr1 = si[len(si)-i-1]

            if ptr0 == ptr1:
                continue
            else:
                return False
        return True

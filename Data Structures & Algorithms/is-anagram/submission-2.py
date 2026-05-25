class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t1 = Counter(t)
        # print(s1)
        # print(t1)
        # reversedS1 = [(values, keys) for keys, values in s1.items()]
        # print(reversedS1)
        return s1 == t1 
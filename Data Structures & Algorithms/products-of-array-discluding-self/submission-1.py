class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # ans = list()

        # temp = 1
        # tempI = 1

        # for i, ivalue in enumerate(nums):
        #     if i == 0:
        #         for j in nums[-1:0:-1]:
        #             temp *= j
        #         ans.append(temp)
        #         temp = 1
        #     else:
        #         # prefix
        #         for j in nums[:i]:
        #             temp *= j

        #         # postfix
        #         for k in nums[i+1:]:
        #             tempI *=k

        #         ans.append(temp*tempI)
        #         temp = 1
        #         tempI = 1

        # return ans

        # This is O(n^2) time. Why not just compute prefix and postfix lastly compute ans. No nested loops

        n = len(nums)
        ans = [0] * n
        prefix = [0] * n
        postfix = [0] *n

        prefix[0] = 1
        postfix[-1] = 1

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n - 2, 0-1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        for i in range(n):
            ans[i] = postfix[i] * prefix[i]
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = list()

        temp = 1
        tempI = 1

        for i, ivalue in enumerate(nums):
            if i == 0:
                for j in nums[-1:0:-1]:
                    temp *= j
                ans.append(temp)
                temp = 1
            else:
                # prefix
                for j in nums[:i]:
                    temp *= j

                # postfix
                for k in nums[i+1:]:
                    tempI *=k

                ans.append(temp*tempI)
                temp = 1
                tempI = 1

                
                


        return ans
            

        
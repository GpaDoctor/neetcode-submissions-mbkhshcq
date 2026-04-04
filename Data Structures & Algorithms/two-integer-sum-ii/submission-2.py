class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        ptr = [0,len(numbers)-1]

        curSum = 0

        while ptr[0] < ptr[1]:
            curSum = numbers[ptr[0]] + numbers[ptr[1]]

            if curSum > target:
                ptr[1] -=1
            elif curSum < target:
                ptr[0] += 1
            else:
                return [ptr[0] +1, ptr[1] + 1]
            
        return []


        
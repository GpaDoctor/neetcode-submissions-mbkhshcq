class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        d = defaultdict(list)

        for i, ivalue in enumerate(numbers):
            complement = target - ivalue
            if d[complement]:
                return [d[complement], i+1]
            d[ivalue] = i+1

        return []

            


        
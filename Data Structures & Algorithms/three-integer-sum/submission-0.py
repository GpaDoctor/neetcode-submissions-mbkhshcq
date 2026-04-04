class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ptr = [0,0]
        ans = set()
        nums.sort()


        for i, ivalue in enumerate(nums):
            # if the ivalue reached +ve, it will never add to be 0, since ptr are both on ivalue right side
            if ivalue > 0: 
                break
            
            # if ivalue is the same as previous, will skip
            if i > 0 and ivalue == nums[i-1]:
                continue
                
            ptr[0], ptr[1] = i + 1, len(nums) -1
            
            while ptr[0] < ptr[1]:
                if nums[ptr[0]] + nums[ptr[1]] + ivalue > 0:
                    ptr[1] -= 1
                elif nums[ptr[0]] + nums[ptr[1]] + ivalue < 0:
                    ptr[0] += 1
                else:
                    res = [ivalue, nums[ptr[0]], nums[ptr[1]]]
                    ans.add(tuple(sorted(res)))
                    ptr[1] -= 1
                    ptr[0] += 1                
        return [list(i) for i in ans]
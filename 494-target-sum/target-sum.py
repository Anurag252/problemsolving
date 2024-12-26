class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def recurse(s, i):
            #print(s,i)
            if i == len(nums)-1:
                if s + nums[i] == target and s - nums[i] == target:
                    return 2
                if s + nums[i] == target or s - nums[i] == target:
                    return 1
                return 0
            res = 0
            
            res = recurse(s + nums[i], i + 1)
            res += recurse(s - nums[i], i + 1)
            
            return res
        return recurse(0, 0)


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        res = 0
        temp = 0
        for k in nums[:-1]:
            temp += k
            if temp >= (s - temp):
                res += 1
        return res
        
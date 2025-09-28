class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(key= lambda x : -x)
        i = 0
        while(i + 2 < len(nums) and nums[i+2] + nums[i+1] <= nums[i]):
            i += 1
        if i + 2 == len(nums):
            return 0
        return nums[i + 1] + nums[i] + nums[i+2]
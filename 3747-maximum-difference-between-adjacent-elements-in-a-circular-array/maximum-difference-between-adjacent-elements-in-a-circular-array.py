class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = 0
        for i, k in enumerate(nums):
            diff = max(diff, abs(nums[i-1] - nums[i]))
        return diff


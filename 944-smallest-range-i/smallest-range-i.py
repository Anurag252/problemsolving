class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        mean_num = (max_num - min_num )/2
        if mean_num < k:
            return 0
        else:
            return max_num - k - min_num - k



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        def search_bin(nums, s, j):
            left = 0
            right = len(nums) - 1

            while(left < right):
                mid = (left + right) // 2
                if nums[mid] > s:
                    right = mid - 1
                else:
                    left = mid + 1
            while left >= 0 and nums[left] >= s:
                left -= 1
            #print(left - j, left, "ll")
            return left - j if left - j >= 0 else 0


        for i, k in enumerate(nums):
            for j, l in enumerate(nums[i+1:]):
                #print(j + i + 1)
                res += search_bin(nums, k + l, j + i + 1)
                #print(res, k, l)
        return res

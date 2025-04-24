class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        unique = len(s)
        res = 0
        for i , k in enumerate(nums):
            a = set()
            for j , l in enumerate(nums[i:]):
                a.add(l)
                if len(a) == unique:
                    print(a, i + j , i)
                    res += (len(nums) - j - i)
                    break
        return res




        
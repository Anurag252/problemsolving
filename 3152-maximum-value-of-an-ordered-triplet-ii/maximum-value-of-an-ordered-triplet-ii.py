class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mx , diff , prod = 0, 0, 0
        pref = [0] * len(nums)
        t = 0
        for i, k in enumerate(nums[::-1]):
            t=max(t, k)
            pref[len(nums) - i-1] = t
        for i, k in enumerate(nums[:-1]):
            if mx > k:
                diff = max(diff, mx - k)
            mx = max(mx, k)
            prod = max(prod, diff * pref[i+1])
        return prod

        
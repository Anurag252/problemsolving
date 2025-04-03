class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mx , diff , prod = 0, 0, 0
        
        for i, k in enumerate(nums):
            prod = max(prod, diff * k)
            diff = max(diff, mx - k)
            mx = max(mx, k)
            
        return prod

        
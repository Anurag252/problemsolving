class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        remainder_count = {}
        # Dictionary to store minimum number for each remainder
        min_number = {}
        
        # Group numbers by remainder and track minimum in each group
        for num in nums:
            r = num % space
            remainder_count[r] = remainder_count.get(r, 0) + 1
            min_number[r] = min(min_number.get(r, float('inf')), num)
        
        max_targets = max(remainder_count.values())
        min_seed = float('inf')
        
        # Find minimum seed that can destroy maximum targets
        for r in remainder_count:
            if remainder_count[r] == max_targets:
                min_seed = min(min_seed, min_number[r])
        
        return min_seed
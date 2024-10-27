class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        from collections import defaultdict

        # Dictionary to count targets destroyed by different starting points
        count_map = defaultdict(int)
        
        # Count how many targets can be destroyed for each starting point
        for num in nums:
            count_map[num % space] += 1

        # Find the maximum number of targets that can be destroyed
        max_destroyed = max(count_map.values())

        # To find the minimum starting point for that max count
        min_value = float('inf')
        for num in nums:
            if count_map[num % space] == max_destroyed:
                min_value = min(min_value, num)

        return min_value
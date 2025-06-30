class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        I conclude that sorting works and order does not matter 
        """
        nums.sort()
        MOD = pow(10,9) + 7

        left = 0
        right = len(nums) - 1
        res = 0
        while(left <= right):
            if nums[left] + nums[right] > target:
                right -= 1 # inc left will only increase sum
            elif nums[left] + nums[right] <= target:
                a = pow(2, right - left) % MOD
                res += a
                res = res % MOD
                left += 1
        return res % MOD
                


            

        
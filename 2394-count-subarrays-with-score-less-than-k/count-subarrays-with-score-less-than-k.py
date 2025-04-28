class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        left = 0
        s = sum(nums)
        total = 0
        res = 0

        for right in range(len(nums)):
            total += nums[right]
            
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            
            res += (right - left + 1)
        
        return res



        right = len(nums) - 1
        
        while(left < len(nums)):
            if s * (right - left + 1) >= k: # still large
                s -= nums[right]
                right -= 1
                if right < 0:
                    left += 1
                    s = left
                    right = left
            else:
                # found max < k

                res += right - left + 1 # nums of subarray
                s -= nums[left]
                left += 1
                while(s * (right - left + 1) <= k and right < len(nums)-1):
                    right += 1
                    s += nums[right]
        return res


        
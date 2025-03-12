class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1 if nums[0] != 0 else 0
        res = 0
        left = 0
        right = len(nums)-1
        while(left + 1 < right):
            
            mid = (left + right) // 2
            if nums[mid] == 0:
                while( mid < len(nums) and nums[mid] == 0):
                    mid += 1
                right = mid
                mid -= 1
                while(mid >= 0 and nums[mid] == 0):
                    mid -= 1
                left = mid
                break

            if nums[mid] < 0:
                left = mid
            else:
                right = mid

        
        if right == len(nums) - 1 and nums[right] < 0: 
            return left + 1 + 1
        if left == 0 and nums[left] > 0:
            return len(nums) - right + 1

        return max(left + 1, len(nums) - right)



        
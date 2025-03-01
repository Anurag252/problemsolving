class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = []

        for i, k in enumerate(nums):
            if i == len(nums) -1 :
                continue
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        for k in nums:
            if k != 0:
                arr.append(k)

        for i in range(len(nums) - len(arr)):
            arr.append(0)
        return arr


        
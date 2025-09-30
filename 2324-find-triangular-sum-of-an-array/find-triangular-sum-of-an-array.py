class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        1
        1 1
        1 2 1 | 1 2 1 - 1 3 3 1
        1 3 3 1 | 1 3 3 1 - 
        1 4 6 4 1
        1 5 10 10 5 1
        1 2*prev 3*prev
        """

        l = len(nums)

        def recurse(nums):
            if len(nums) == 1:
                return nums[0] % 10
            arr = []
            for i in range(0, len(nums)-1):
                arr.append( (nums[i] + nums[i+1]) % 10)
            return recurse(arr)
        return recurse(nums)



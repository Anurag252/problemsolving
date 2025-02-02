class Solution:
    def check(self, nums: List[int]) -> bool:
        inflextion = False
        for idx, k in enumerate(nums):
            if idx == 0:
                continue
            if k < nums[idx-1] and  inflextion:
                return False
            if k >= nums[idx-1] and not inflextion:
                continue
            else :
                inflextion = True

        if inflextion and nums[-1] > nums[0]:
            return False
        return True



        
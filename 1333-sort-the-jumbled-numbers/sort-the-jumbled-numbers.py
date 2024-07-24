class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def srt(x):
            result = 0
            mul = 1
            if x == 0:
                return mapping[0]
            while x > 0:
                y = x%10
                result = result + mul*mapping[y]
                mul = mul * 10
                x = int(x /10)
            return result
        nums=sorted(nums,reverse=False, key=srt)
        return nums
            

        
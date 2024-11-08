class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        largestnum = 2 ** maximumBit - 1
        res = []
        n = nums


        a =[nums[0]]

        for idx, k in enumerate(nums):
            if idx == 0:
                continue
            a.append(a[-1] ^ k)


        for idx, l in enumerate(a):
            res.append(largestnum - l)
        res.reverse()
        return res


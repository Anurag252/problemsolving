class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant = -1
        count = -1
        temp = {}
        for k in nums:
            if k not in temp:
                temp[k] = 0
            temp[k] += 1
        print(temp)
        for k in temp:
            if count < temp[k]:
                dominant = k
                count = temp[k]
        print(dominant)

        nc = 0
        for i, k in enumerate(nums):
            if k == dominant:
                nc += 1
            if nc > math.floor((i + 1) / 2) and count - nc > math.floor((len(nums) - i - 1) / 2):
                return i
        return -1


        
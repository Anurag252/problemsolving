class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        i = 0
        j = 0
        arr = []
        while i < len(nums):
            j = i
            sum1 = 0
            while j < len(nums):
                sum1 += nums[j]
                arr.append(sum1)
                j += 1
            i += 1
        
        arr.sort()
        k = arr[left-1:right]
        x = sum(k)
        return x %  (pow(10,9) + 7)




        
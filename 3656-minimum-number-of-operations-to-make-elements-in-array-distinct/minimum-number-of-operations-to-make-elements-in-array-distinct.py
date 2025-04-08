class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = [0] * 101

        for i in nums:
            arr[i] += 1
        start = 0
        for k in range(0,100):
            found = False
            for m in range(0,100):
                if arr[m] > 1:
                    found= True
                    break
            if not found:
                return k 
            if start + 2 >= len(nums):
                return k + 1
            arr[nums[start]] -= 1
            arr[nums[start+ 1]] -= 1
            arr[nums[start+ 2]] -= 1
            start += 3
        return 100


        
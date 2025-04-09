class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # keep fetching the largest elements and keep changing them to 
        # h
        # at the end res is num of unique elements > k

        s = set(nums)
        count = 0
        c = 0
        if k > min(nums):
            return -1
        for m in nums:
            if m == k:
                c += 1
        if c == len(nums):
            return 0

        for m in s:
            if m > k:
                count += 1
            
            
       
        return count if count > 0 else -1

        
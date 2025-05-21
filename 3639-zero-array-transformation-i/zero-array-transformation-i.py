class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        every element has x numbers of reductions 
        to find the number of reductions, process all elements and find the number of reductions
        it will be slow if we just apply the chnages one by one
        another way could be put -1 at the start and + 1 at the end

        """
        arr = [0] * len(nums)

        for k in queries:
            arr[k[0]] += 1
            if k[1] + 1 < len(nums):
                arr[k[1] + 1] -= 1
            

        subs = 0
        for i , k in enumerate(nums):
            subs += arr[i]
            if nums[i] != 0:
                nums[i] -= min(nums[i], subs)
            
            
        print(nums, arr)
        for k in nums:
            if k != 0:
                return False
        return True
            

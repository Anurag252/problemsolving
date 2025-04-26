class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # consider the elements mark min and max
        # also mark lower and upper numbers as 0  
        # now we need sub arrays that include min amd max - a....b...c...d -> d - a 
        # other possibility is a .... b ....d....c -? no subarray 
        for i, k in enumerate(nums):
            if k < minK or k > maxK:
                nums[i] = 0

        left = 0
        right = 0
        founda = -1  # Index of last minK
        foundb = -1  # Index of last maxK
        res = 0
        nums = [0] + nums + [0]  # Add boundary zeros

        for i in range(len(nums)):
            if nums[i] == 0:
                left = i
                founda = -1
                foundb = -1
            else:
                if nums[i] == minK:
                    founda = i
                if nums[i] == maxK:
                    foundb = i
                if founda != -1 and foundb != -1:
                    res += min(founda, foundb) - left

        return res
        for i, k in enumerate(nums):
            if k < minK:
                nums[i] = 0
            if k > maxK:
                nums[i] = 0

        
        left = 0
        right = 0
        founda = False
        foundb = False
        res = 0
        nums = [0] + nums + [0]
        while(right >= left and left < len(nums) and right < len(nums)):

            if nums[right] == minK:
                founda = True

            if nums[right] == minK:
                foundb = True

            if nums[right] == 0 and right > left:
                print("a", right, left)
                res += right - left - 1
                left = right
                founda = False
                foundb = False
                continue

            if nums[left] == 0:
                right += 1
                continue
            
        return res 

            

            

            

        
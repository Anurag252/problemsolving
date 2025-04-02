class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pos = [0] * len(nums)
        
        temp1 = 0
        temp2 = 0
        for i, k in enumerate(nums[::-1]):
            if temp1 < k:
                temp1 = k
            pos[len(nums) - i-1] = temp1
            
        #print(pos, neg)
        mx = 0
        for i , k1 in enumerate(nums):
            if i + 1 >= len(nums):
                continue
            for j, k2 in enumerate(nums[i+1:]):
                if i+1 + j+1 < len(nums):
                    #print(i,j)
                    mx = max(mx, (k1 - k2) * pos[i+1 + j+1])
        return mx

        
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = sum(nums[:k])
        dic = {}
        for m in nums[:k]:
            if m not in dic:
                dic[m] = 1
            else:
                dic[m] += 1
        
        print(nums[:k])
        start = 0
        ans = 0
        
        while(start + k < len(nums) ):
            #print(s, sum(arr))
            if len(dic) == k:
                ans = max(ans, s)
            s -= nums[start]
            dic[nums[start]] -= 1
            if dic[nums[start]] == 0:
                del dic[nums[start]]
 
            s += nums[start + k]
            if nums[start + k] not in dic:
                dic[nums[start + k]] = 1
            else:
                dic[nums[start + k]] += 1
            start += 1
            

        if len(dic) == k:
                ans = max(ans, s)
        return ans


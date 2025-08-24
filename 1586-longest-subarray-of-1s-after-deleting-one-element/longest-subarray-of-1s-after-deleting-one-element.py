class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pref = []
        suff = []
        temp = 0
        for k in nums:
            if k == 0:
                temp = 0
            else:
                temp += 1
            pref.append(temp)
        temp = 0
        for k in nums[::-1]:
            if k == 0:
                temp = 0
            else:
                temp += 1
            suff.append(temp)
        suff.reverse()
        print(nums, pref)
        try:
            nums.index(0) # no zeros
            res = 0
            for i, k in enumerate(nums):
                if k == 0 and i + 1 < len(suff) and i - 1 >= 0 :
                    res = max(res, pref[i-1] + suff[i+1])
                elif k == 0 :
                    if i + 1 >= 0:
                        res = max(res, pref[i-1])
                    else:
                        rews = max(res, suff[i+1])
            return res
        except:
             return sum(nums) - 1



        
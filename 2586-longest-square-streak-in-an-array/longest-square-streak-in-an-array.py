class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        mp = {}
        for k in nums:
            s = int(math.sqrt(k))
            print(s,math.sqrt(k), s == math.sqrt(k) )
            if s in mp and s == math.sqrt(k):
                mp[k] = (mp[s] + 1)
                res.append(mp[k])
                
            else:
                mp[k] = 0
        #print(res, mp)
        return max(res) +  1 if len(res) > 0 else -1


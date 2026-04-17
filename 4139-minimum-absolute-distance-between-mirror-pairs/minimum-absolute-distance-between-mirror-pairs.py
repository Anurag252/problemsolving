class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}
        res = 1000000

        for i, k in enumerate(nums):
            t = list(str(k))
            t.reverse()
            t = int("".join(t))

            if t % 10 == 0:
                t = t // 10
            
            if k in mp:
                res = min(res, abs(mp[k] - i))
            mp[t] = i
            #print(t, mp, res, k)
        return res if res < 1000000 else -1

        
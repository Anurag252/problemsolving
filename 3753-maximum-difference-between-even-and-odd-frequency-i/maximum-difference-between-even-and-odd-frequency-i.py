class Solution:
    def maxDifference(self, s: str) -> int:
        mp = {}

        for k in s:
            if k not in mp:
                mp[k] = 0
            mp[k] += 1
        even = 100000
        odd = 0
        for k, v in mp.items():
            if v % 2 == 0:
                even = min(even, v)
            else:
                odd = max(odd, v)
        return odd - even

        
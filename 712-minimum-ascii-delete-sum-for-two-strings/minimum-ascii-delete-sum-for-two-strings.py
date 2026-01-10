class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        res = 0
        # order matters
        # if char does not exists then we must delete 
        # if it occurs at multiple places we must backtrack to find which eads to same str
        # since asciss sum means same chars , no need to look for smallest chars
        @cache
        def recurse(s1, s2,  i, j):
            if i == len(s1) and j == len(s2):
                return 0
            if i == len(s1):
                res = 0
                for k in s2[j:]:
                    res += ord(k)
                return res
            if j == len(s2):
                res = 0
                for k in s1[i:]:
                    res += ord(k)
                return res
            if s1[i:] == s2[j:]:
                return 0
            if s1[i] == s2[j]:
                return recurse(s1, s2, i + 1, j + 1)
            else:
                return min(ord(s1[i]) + recurse(s1, s2, i + 1, j) , ord(s2[j]) + recurse(s1, s2, i , j + 1))

        return recurse(s1, s2, 0, 0)
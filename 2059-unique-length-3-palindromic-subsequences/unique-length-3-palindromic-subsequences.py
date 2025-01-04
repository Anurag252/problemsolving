class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        arr = [(-1,-1)] * 26
        #suff.reverse()

        for idx, k in enumerate(s):
            if arr[ord(k) - ord('a')] == (-1,-1):
                arr[ord(k) - ord('a')] = (idx, -1)
            else:
                arr[ord(k) - ord('a')] = (arr[ord(k) - ord('a')][0], idx)
        # there may a problem of duplicates - will not  be
        res = 0
        for (k0, k1) in arr:
            if k0 >= 0 and k1 >= 0 and k1 > k0 + 1:
                st = set()
                for m in s[k0+1:k1]:
                    st.add(m)
                res += (len(st))
        return res



        
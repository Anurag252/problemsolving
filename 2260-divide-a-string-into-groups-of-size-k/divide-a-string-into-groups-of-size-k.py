class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = 0
        res = []
        while(l + k < len(s)):
            t = s[l:l+k]
            res.append(t)
            l += k
        res.append(s[l:] + str(fill * (l + k - len(s))))
        return res




        
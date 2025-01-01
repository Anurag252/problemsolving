class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        left = []
        right = []
        temp0 = 0
        temp1 = 0
        for k in s:
            if k == "0":
                temp0 += 1
            left.append(temp0)
            if k == "1":
                temp1 += 1
            right.append(temp1)


        for idx, (k1, k2) in enumerate(zip(left, right)):
            if idx == len(right)-1:
                continue
            res = max(res, k1 + right[-1] - right[idx])
        return res



        
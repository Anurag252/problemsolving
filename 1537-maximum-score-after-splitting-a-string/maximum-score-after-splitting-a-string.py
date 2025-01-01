class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        left = []
        right = []
        temp = 0
        for k in s:
            if k == "0":
                temp += 1
            left.append(temp)

        temp = 0
        for k in s[::-1]:
            if k == "1":
                temp += 1
            right.append(temp)
        right.reverse()

        for idx, (k1, k2) in enumerate(zip(left, right)):
            if idx == len(right)-1:
                continue
            res = max(res, k1 + right[idx + 1])
        return res



        
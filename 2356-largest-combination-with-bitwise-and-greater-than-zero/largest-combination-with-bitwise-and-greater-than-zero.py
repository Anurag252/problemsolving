class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 24
        t = 1
        for i in range(1,25):
            for k in candidates:
                if k & t != 0:
                    res[i-1] += 1
            t = t << 1
        return max(res)
        


        
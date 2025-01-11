class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        dt = {}
        count_one = 0
        for m in s:
            if m not in dt:
                dt[m] = 0
            dt[m] += 1
        
        for v in dt.values():
            if v % 2 == 1:
                count_one += 1
        
        if k > len(s) or k - count_one < 0:
            return False
        return True

        
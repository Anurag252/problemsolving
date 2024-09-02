class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k >= sum(chalk):
            k = k % sum(chalk)
        
        for idx, m in enumerate(chalk):
            k = k - m
            if k < 0:
                return idx
        
        
        
        
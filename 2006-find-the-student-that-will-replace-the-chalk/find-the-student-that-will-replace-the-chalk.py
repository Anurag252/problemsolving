class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k >= sum(chalk):
            k = k % sum(chalk)
        pre_sum = [0] * len(chalk)
        s = 0
        for idx, m in enumerate(chalk):
            s += m
            pre_sum[idx] = s
        
        start = 0
        end = len(chalk) - 1
        while(start < end):
            mid = int((end + start) / 2)
            #print(mid)
            if pre_sum[mid] > k and pre_sum[mid-1] <= k:
                return mid
            if pre_sum[mid] == k:
                return mid + 1
            if pre_sum[mid] > k:
                end = mid-1
            if pre_sum[mid] < k:
                start = mid+1
        return start
            
        
        
        
        
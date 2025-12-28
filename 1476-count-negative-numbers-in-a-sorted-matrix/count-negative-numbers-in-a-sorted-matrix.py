class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for k in grid:
            left = 0
            right = len(k) - 1
            if k[right] >= 0:
                continue
            while(left < right):
                print(left, right)
                mid = (right + left) // 2
                if k[mid] < 0:
                    right = mid 
                else :
                    left = mid + 1
            ans += (len(k)   - right )
            #print(len(k)  - right)
        return ans
            
            
        
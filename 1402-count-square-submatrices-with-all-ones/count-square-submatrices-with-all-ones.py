from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_bound = len(matrix)
        col_bound = len(matrix[0])
        
        # Create DP matrix initialized to zero
        dp = [[0] * col_bound for _ in range(row_bound)]
        count = 0
        
        for i in range(row_bound):
            for j in range(col_bound):
                # Only consider if matrix[i][j] is 1
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:  # Base case for first row/column
                        dp[i][j] = 1
                    else:
                        # Minimum of top, left, and top-left + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Add to count of squares
                    count += dp[i][j]
        
        return count

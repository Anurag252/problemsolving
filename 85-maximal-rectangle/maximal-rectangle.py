class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [[0] * cols for _ in range(rows)]
        
        # Build row histograms
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[i][j] = 1 if i == 0 else heights[i-1][j] + 1
        
        # Compute maximal rectangle for each row
        max_area = 0
        for i in range(rows):
            for start_col in range(cols):
                if heights[i][start_col] == 0:
                    continue
                min_height = heights[i][start_col]
                for end_col in range(start_col, cols):
                    if heights[i][end_col] == 0:
                        break
                    min_height = min(min_height, heights[i][end_col])
                    width = end_col - start_col + 1
                    max_area = max(max_area, width * min_height)

        return max_area

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
            diagonals have 
            0,2
            0,1 1,2
            0,0 1,1 2,2
            1,0 2,1
            2,0

            start with each cell in first row and keep adding 1,1 till we hit the boundary
        """
        n = len(grid)
        for k in range(n):
            arr = []
            i = 0
            j = k
            
            while(i < n and j < n):
                arr.append(grid[i][j])
                i += 1
                j += 1
            arr.sort(key=lambda x : x)
            print(arr)
            i = 0
            j = k
            l = 0
            while(i < n and j < n):
                grid[i][j] = arr[l]
                l += 1
                i += 1
                j += 1

        for k in range(n):
            arr = []
            i = k
            j = 0
            
            while(i < n and j < n):
                arr.append(grid[i][j])
                i += 1
                j += 1
            arr.sort(key=lambda x : -x)
            print(arr)
            i = k
            j = 0
            l = 0
            while(i < n and j < n):
                grid[i][j] = arr[l]
                l += 1
                i += 1
                j += 1
        return grid

        
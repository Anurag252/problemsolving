
func dfs_row(row int, col int, grid [][]int, found bool) (int ) {
    res := 0
    
    for k , v := range grid[row] {
       if v == 1 {
        grid[row][k] = 0
        res += res + 1+ dfs_row(row, k , grid, true)
       }
    }

    for a := range len(grid) {
        if grid[a][col] == 1 {
            grid[a][col] = 0
            res = res + 1 +  dfs_row(a, col , grid, true)
            //grid[a][col] = 1
        }
    }
    if !found && res == 1 {
        return 0
    }
    return res

}



func countServers(grid [][]int) int {

    res := 0
    //mp := make(map[int]int, 0)
    for i , _ := range grid {
        for j , _ := range grid[0] {
            if grid[i][j] == 1 {
                res += dfs_row(i,j,grid, false)
            }
            
        }
    }
    
    return res
}
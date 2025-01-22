func highestPeak(isWater [][]int) [][]int {
    m, n := len(isWater), len(isWater[0])
    res := make([][]int, m)
    queue := [][]int{}

    for i := 0; i < m; i++ {
        res[i] = make([]int, n)
        for j := 0; j < n; j++ {
            if isWater[i][j] == 1 {
                res[i][j] = 0
                queue = append(queue, []int{i, j})
            } else {
                res[i][j] = -1
            }
        }
    }

    dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    for len(queue) > 0 {
        cell := queue[0]
        queue = queue[1:]
        i, j := cell[0], cell[1]

        for _, d := range dirs {
            ni, nj := i + d[0], j + d[1]
            if ni >= 0 && ni < m && nj >= 0 && nj < n && res[ni][nj] == -1 {
                res[ni][nj] = res[i][j] + 1
                queue = append(queue, []int{ni, nj})
            }
        }
    }

    return res
}
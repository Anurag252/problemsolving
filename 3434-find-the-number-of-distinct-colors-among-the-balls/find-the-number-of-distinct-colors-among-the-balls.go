func queryResults(limit int, queries [][]int) []int {
    balls := make(map[int]int)
    colors := make(map[int]int)
    res := make([]int, 0)
    for _, k := range queries {
        col , ok := balls[k[0]]
        if ! ok {
            balls[k[0]] = k[1]
            _, ok = colors[k[1]]
            if !ok {
                colors[k[1]] = 1
            } else {
                colors[k[1]] += 1
            }
            
        } else {
            balls[k[0]]  = k[1]
            colors[col] -= 1
            if colors[col] == 0 {
                delete(colors, col)
            }
            _, ok = colors[k[1]]
            if !ok {
                colors[k[1]] = 1
            } else {
                colors[k[1]] += 1
            }

        }
        //fmt.Println(colors)
        res = append(res, len(colors))
        
    }
    
    return res
}
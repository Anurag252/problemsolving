func firstCompleteIndex(arr []int, mat [][]int) int {
    // cache row and col for all elements from mat
    // maintain another arr of row , and col sizes and initialize each element to col and row 
    // read the arr and reduce each row and col , when you reach till 0 return
    
    mp := make(map[int]string)
    for a, _ := range mat {
        for b, j := range mat[a] {
            //fmt.Println(strconv.Itoa(a) + "$" + strconv.Itoa(b))
            mp[j] = strconv.Itoa(a) + "$" + strconv.Itoa(b)
        }
    }
    //fmt.Println(mp)

    row := make([]int, len(mat))
    col := make([]int, len(mat[0]))

    for a, _ := range row {
        row[a] = len(mat[0])
    }

    for a, _ := range col {
        col[a] = len(mat)
    }

    for i, elem := range arr {
        parts := mp[elem]
        r, _ := strconv.Atoi(strings.Split(parts, "$")[0])
        c, _  := strconv.Atoi(strings.Split(parts, "$")[1])
        row[r] --
        if row[r] == 0 {
            return i
        }

        col[c] --
        if col[c] == 0 {
            return i
        }
    }

    return -1
}
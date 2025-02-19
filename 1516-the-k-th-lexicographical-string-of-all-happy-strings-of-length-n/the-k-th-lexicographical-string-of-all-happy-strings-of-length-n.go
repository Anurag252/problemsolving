import "sort"
func getHappyString(n int, k int) string {
    str := []string{"a", "b", "c"}
    // list of n is a appended to n-1 list with restrictions
    res := calc(str, n)
    sort.Strings(res)
    if len(res) > k - 1 {
        return res[k- 1]
    }
    return ""
}

func calc(str []string, n int) []string {
    if n == 1 {
        return str
    }
    newRes := make([]string, 0)
    res := calc(str, n-1)
    for _, k := range res {
        for _, k1 := range str {
                if string(k[0]) != k1 {
                newRes = append(newRes, k1 + k)
            }
        }
        
    }
    return newRes
}
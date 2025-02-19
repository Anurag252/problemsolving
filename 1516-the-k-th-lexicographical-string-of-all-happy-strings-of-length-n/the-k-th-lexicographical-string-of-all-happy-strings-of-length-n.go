//import "sort"
func getHappyString(n int, k int) string {
    str := []string{"a", "b", "c"}
    // list of n is a appended to n-1 list with restrictions
    res := calc(str, n) //T[n] = 2*T[n-1] or  4*T[n-2] or 8*T[n-3] ..., T[n-1] = 2*T[n-2] -> 2^n
    // 2^10 is 1024
    //sort.Strings(res) // klogk
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
                if string(k[len(k)-1]) != k1 {
                newRes = append(newRes,k + k1)
            }
        }
        
    }
    return newRes
}
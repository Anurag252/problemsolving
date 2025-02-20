func findDifferentBinaryString(nums []string) string {
    arr := []string{"0","1"}

    n := len(nums)
    if n == 1 {
        if nums[0] == "0" {
            return "1"
        } else {
            return "0"
        }
        
    }
    mp := make(map[string]bool)

    for _, k := range nums {
        mp[k] = true
    }

    return calc(arr, n-1, arr, mp)
}

func calc(arr []string, n int, prev []string, mp map[string]bool) string {
    if n == 1 {
        for _, k := range prev {
            for _, k1 := range arr {
                _, ok := mp[k + k1]
                if !ok {
                    return k + k1
                }
            }
            
        }
    }
    t := make([]string, 0)
    for _, k1 := range arr {
        for _, k := range prev {
            t = append(t, k1 + k)
        }
    }
    return calc(arr, n-1 , t, mp)

}
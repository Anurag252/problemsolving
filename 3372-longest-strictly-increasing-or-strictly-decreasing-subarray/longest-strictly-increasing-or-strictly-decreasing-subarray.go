func longestMonotonicSubarray(nums []int) int {
    l := 0
    prev := -1
    res := 0
    for _ , k := range nums {
        if prev < k {
            l += 1
            prev = k
        } else {
            res = max(res, l)
            l = 1
            prev = k
        }
    }
    res = max(res, l)
    prev = -1
    l = 0
    
    //fmt.Println(nums)
    for _ , k := range nums {
        if prev > k {
            l += 1
            prev = k
        } else {
            res = max(res, l)
            l = 1
            prev = k
        }
    }
    res = max(res, l)
    return res
}
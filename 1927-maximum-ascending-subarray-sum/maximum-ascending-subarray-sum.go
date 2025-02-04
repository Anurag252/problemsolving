func maxAscendingSum(nums []int) int {
    s := 0
    prev := -1
    res := 0
    for _, k := range nums {
        if prev < k {
            s += k
            prev = k
        } else {
            res = max(res, s)
            s = k
            prev = k
        }
    }

     res = max(res, s)
     return res
}


func maximumSum(nums []int) int {
    mp := make(map[int][]int)

    for i , k := range nums {
        n := 0
        for(k > 0) {
            n += (k % 10)
            k = k / 10
        }
        _, ok := mp[n]
        if ok {
            mp[n] = append(mp[n], i)
        } else {
            mp[n] = make([]int, 0)
            mp[n] = append(mp[n], i)
        }
    }
    //fmt.Println(mp)

    res := -1
    for _,v := range mp {
        if len(v) >= 2 {
            m1 := 0

            m2 := 0

            for _, c := range v {
                if nums[c] > m1 {
                    m2 = max(m2, m1)
                    m1 = nums[c]
                } else {
                    m2 = max(nums[c], m2)
                }

            }

            res = max(res, m1 + m2)
        }
    }
    return res
}
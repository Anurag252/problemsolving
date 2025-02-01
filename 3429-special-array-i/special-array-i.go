func isArraySpecial(nums []int) bool {
    t := nums[0]
    isEven := false // odd

    if t & 1 == 0 { // even
        isEven = true
    }

    // 1 0 1 0 1 0
    // 0 1 0 1 0 1

    for _ , k := range nums {
        
        if ( ((k & 1) == 0 &&  isEven ) || ((k & 1) == 1 &&  !isEven ) ) {
            isEven = !isEven
        } else {
            return false
        }
        
       
        //fmt.Println(t, k, k & 1)
        
    }
    return true
}
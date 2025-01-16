func xorAllNums(nums1 []int, nums2 []int) int {
    
    // if num2 is even times and num 1 is odd times then num2 is answer
    // num2 is even and num1 is even then ans is 0
    // if both are odd then do all xor ^ firste elem ^ ...
    if len(nums1) % 2 == 0 && len(nums2) % 2 == 0 {
        return 0
    }

    

    temp2 := nums2[0]
    for i := 1; i < len(nums2) ; i ++ {
        temp2 ^= nums2[i]
    }

   

    temp1 := nums1[0]

    for i := 1 ; i < len(nums1) ; i ++ {
        temp1 ^= nums1[i]
    }
     if len(nums1) % 2 == 0 && len(nums2) % 2 != 0 {
        return temp1
    }

     if len(nums1) % 2 != 0 && len(nums2) % 2 == 0 {
        return temp2
    }
    return temp1 ^ temp2
}
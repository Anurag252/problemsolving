func findThePrefixCommonArray(A []int, B []int) []int {
    mp := make([]int, len(A))

    res := make([]int, len(A))

    temp := 0

    for i , _ := range A {
        mp[A[i]-1] += 1
        mp[B[i]-1] += 1

        if mp[A[i]-1] == 2 {
            temp += 1
            mp[A[i]-1] = 0
        }

        if mp[B[i]-1] == 2 {
            temp += 1
            mp[B[i]-1] = 0
        }
        res[i] = temp
    }
    return res
}
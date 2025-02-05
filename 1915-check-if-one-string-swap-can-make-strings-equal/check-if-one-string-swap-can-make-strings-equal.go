func areAlmostEqual(s1 string, s2 string) bool {
    
    diff1 := make([]rune, 0)
    diff2 := make([]rune, 0)
    for i , k := range s1 {
        if rune(s2[i]) != k {
            diff1 = append(diff1, k)
            diff2 = append(diff2, rune(s2[i]) )
        }
    }

    if len(diff1) == 0 {
        return true
    }

    if len(diff1) == 1 {
        return false
    }

    if diff1[0] == diff2[1] && diff1[1] == diff2[0] && len(diff1) == 2 {
        return true
    }
    return false
}
func getLucky(s string, k int) int {
    result := ""
    for _,m := range s{
        i := int(m - 96)
        fmt.Println(i)
        result = result + strconv.Itoa(i)
    }
    
    
    for i := 0 ; i < k ; i ++ {
        fmt.Println(result)
        sum := 0
        for result != "" {
            m, _ := strconv.Atoi(string(result[len(result) - 1]))
            sum += m
            result = result[:len(result) - 1]
        }
        result = strconv.Itoa(sum)
    }
    ans,_ := strconv.Atoi(result)
    return ans
    
}
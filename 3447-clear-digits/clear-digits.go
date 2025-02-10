func clearDigits(s string) string {
    st := make([]rune,0)
    for _ , k := range s {
        _, err := strconv.Atoi(string(k))
        if err == nil {
            if len(st) > 0 {
                st = st[:len(st)-1]
            }
        } else {
            st = append(st , k)
        }
    }

    m := ""
    for _, k := range st {
        m += string(k)
    }
    return m
}
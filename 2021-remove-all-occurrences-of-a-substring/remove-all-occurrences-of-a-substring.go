import (
    "strings"
)

func removeOccurrences(s string, part string) string {
    // in case we do a recursive func, we get n/2 * m 
    // another approach is maybe brackets balancing like stack
    // that is m + n efficient ?def more than first approach

    st := make([]string, 0)

    for _, k := range s {
        if len(st) >= len(part) {
            last := st[len(st) - len(part):]
            //fmt.Println(last, st)
            if strings.Join(last, "") == part {
                st = st[:len(st) - len(part)]
            } 
        }
        st = append(st, string(k))
        
    }
    if len(st) >= len(part) {
            last := st[len(st) - len(part):]
            fmt.Println(last, st)
            if strings.Join(last, "") == part {
                st = st[:len(st) - len(part)]
            } 
        }
    return strings.Join(st, "")

}
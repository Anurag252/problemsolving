func dfs(source int, adj map[int][]int , visited map[int]bool, parent int) bool {
    //fmt.Println(visited, source, adj)
    _, ok := visited[source]
    
    if ok  {
        
        return false
    }
    visited[source] = true
    
    for _, k := range adj[source] {
        if parent != k && ! dfs (k, adj, visited, source)  {
            return false
        }
    }
    return true
}

func findRedundantConnection(edges [][]int) []int {
    
    adj := make(map[int][]int)

    for _, k := range edges {
        _, ok := adj[k[0]]
        if ! ok {
            adj[k[0]] = make([]int, 0)
            adj[k[0]] = append(adj[k[0]], k[1])
        } else {
            adj[k[0]] = append(adj[k[0]], k[1])
        }


        _, ok = adj[k[1]]
        if ! ok {
            adj[k[1]] = make([]int, 0)
            adj[k[1]] = append(adj[k[1]], k[0])
        } else {
            adj[k[1]] = append(adj[k[1]], k[0])
        }

        visited := make(map[int]bool)
        //fmt.Println("andy")
        if ! dfs(k[0], adj, visited, -1) {
            return k
        }
    }

    return nil
}
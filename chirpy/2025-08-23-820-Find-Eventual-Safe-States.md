---
            title: "820 Find Eventual Safe States"
            date: "2025-08-23T09:18:29+02:00"
            categories: ["leetcode"]
            tags: [csharp]
            layout: post
---
            
## [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a **0-indexed** 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return *an array containing all the **safe nodes** of the graph*. The answer should be sorted in **ascending** order.

 

Example 1:

![image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)
```

**Input:** graph = [[1,2],[2,3],[5],[0],[5],[],[]]
**Output:** [2,4,5,6]
**Explanation:** The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
```

Example 2:

```

**Input:** graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
**Output:** [4]
**Explanation:**
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

```

 

**Constraints:**

	n == graph.length
	1 <= n <= 104
	0 <= graph[i].length <= n
	0 <= graph[i][j] <= n - 1
	graph[i] is sorted in a strictly increasing order.
	The graph may contain self-loops.
	The number of edges in the graph will be in the range [1, 4 * 104].

{% raw %}


```csharp


public class Solution 
{
    enum Marking
    {
        Unvisited = 0,
        Temporary = 1,
        Visited = 2
    }    
    
    public IList<int> EventualSafeNodes(int[][] graph) 
    {
        Marking[] markings = new Marking[graph.Length];
        List<int> result = new List<int>();
        
        for(int i = 0; i < graph.Length; i++)
        {
            if(!detectCycle(graph, i, markings))
            {
                result.Add(i);        
            }
        }
        
        return result;
    }
    
    private bool detectCycle(int[][] graph, int node, Marking[] markings)
    {
        if(markings[node] == Marking.Temporary)
        {
            return true;
        }
        
        if(markings[node] == Marking.Visited)
        {
            return false;
        }
        
        markings[node] = Marking.Temporary;
        
        foreach(int neighbour in graph[node])
        {   
            if(detectCycle(graph, neighbour, markings))
            {
                return true;
            }            
        }       
        
        markings[node] = Marking.Visited;
        return false;        
    }
}


{% endraw %}
```

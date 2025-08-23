---
            title: "2090 Number Of Ways To Arrive At Destination"
            date: "2025-08-23T13:42:46+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

You are in a city that consists of n intersections numbered from 0 to n - 1 with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the **shortest amount of time**.

Return *the **number of ways** you can arrive at your destination in the **shortest amount of time***. Since the answer may be large, return it **modulo** 109 + 7.

 

Example 1:

![image](https://assets.leetcode.com/uploads/2025/02/14/1976_corrected.png)
```

**Input:** n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
**Output:** 4
**Explanation:** The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

```

Example 2:

```

**Input:** n = 2, roads = [[1,0,10]]
**Output:** 1
**Explanation:** There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

```

 

**Constraints:**

	1 <= n <= 200
	n - 1 <= roads.length <= n * (n - 1) / 2
	roads[i].length == 3
	0 <= ui, vi <= n - 1
	1 <= timei <= 109
	ui != vi
	There is at most one road connecting any two intersections.
	You can reach any intersection from any other intersection.

{% raw %}


```python


import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]  # (time, node)

        while heap:
            curr_time, node = heapq.heappop(heap)
            if curr_time > dist[node]:
                continue
            for nei, t in graph[node]:
                new_time = curr_time + t
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[n - 1]



{% endraw %}
```

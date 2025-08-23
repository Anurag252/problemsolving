---
            title: "1485 Minimum Cost To Make At Least One Valid Path In A Grid"
            date: "2025-08-23T09:18:29+02:00"
            categories: ["leetcode"]
            tags: [cpp]
            layout: post
---
            
## [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid) ![image](https://img.shields.io/badge/Difficulty-Hard-red)

Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

	1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
	2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
	3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
	4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell **one time only**.

Return *the minimum cost to make the grid have at least one valid path*.

 

Example 1:

![image](https://assets.leetcode.com/uploads/2020/02/13/grid1.png)
```

**Input:** grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
**Output:** 3
**Explanation:** You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

```

Example 2:

![image](https://assets.leetcode.com/uploads/2020/02/13/grid2.png)
```

**Input:** grid = [[1,1,3],[3,2,2],[1,1,4]]
**Output:** 0
**Explanation:** You can follow the path from (0, 0) to (2, 2).

```

Example 3:

![image](https://assets.leetcode.com/uploads/2020/02/13/grid3.png)
```

**Input:** grid = [[1,2],[4,3]]
**Output:** 1

```

 

**Constraints:**

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 100
	1 <= grid[i][j] <= 4

{% raw %}


```cpp


constexpr int MAX_N = 101;
constexpr int MAX_F = 2 * MAX_N;


constexpr int DR[] = {0, 0, 1, -1};
constexpr int DC[] = {1, -1, 0, 0};

class Solution {
    int m, n;
    vector<vector<int>> G;
    int dp[MAX_N][MAX_N][MAX_F] = {};
    bool seen[MAX_N][MAX_N][MAX_F] = {};

    bool valid(int r, int c) {
        return 0 <= r && r < m && 0 <= c && c < n;
    }

    int dfs(int r, int c, int fuel) {
        if (fuel >= MAX_F)
            return INT_MAX;
        if (r == m - 1 && c == n - 1)
            return fuel;
        // if (dp[r][c][fuel] != -1)
        //     return dp[r][c][fuel];
        if (seen[r][c][fuel])
            return INT_MAX;
        seen[r][c][fuel] = true;
        int d = G[r][c] - 1;
        int rr = r + DR[d];
        int cc = c + DC[d];
        int best = INT_MAX;
        if (valid(rr, cc))
            best = min(best, dfs(rr, cc, fuel));
        for (d = 0; d < 4; d++) {
            rr = r + DR[d];
            cc = c + DC[d];
            if (valid(rr, cc)) {
                int t = dfs(rr, cc, fuel + 1);
                best = min(best, t == INT_MAX ? INT_MAX : t);
            }
        }
        return best;
    }
public:
    int minCost(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        G = grid;
        for (int r = 0; r < MAX_N; r++)
            for (int c = 0; c < MAX_N; c++)
                for (int f = 0; f < MAX_F; f++)
                    dp[r][c][f] = -1;
        return dfs(0, 0, 0);
    }
};


{% endraw %}
```

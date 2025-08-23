---
            title: "1876 Map Of Highest Peak"
            date: "2025-08-23T13:42:46+02:00"
            categories: ["leetcode"]
            tags: [go]
            layout: post
---
            
## [Map of Highest Peak](https://leetcode.com/problems/map-of-highest-peak) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

You are given an integer matrix isWater of size m x n that represents a map of **land** and **water** cells.

	If isWater[i][j] == 0, cell (i, j) is a **land** cell.
	If isWater[i][j] == 1, cell (i, j) is a **water** cell.

You must assign each cell a height in a way that follows these rules:

	The height of each cell must be non-negative.
	If the cell is a **water** cell, its height must be 0.
	Any two adjacent cells must have an absolute height difference of **at most** 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is **maximized**.

Return *an integer matrix *height* of size *m x n* where *height[i][j]* is cell *(i, j)*'s height. If there are multiple solutions, return **any** of them*.

 

Example 1:

**![image](https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png)**

```

**Input:** isWater = [[0,1],[0,0]]
**Output:** [[1,0],[2,1]]
**Explanation:** The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

```

Example 2:

**![image](https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png)**

```

**Input:** isWater = [[0,0,1],[1,0,0],[0,0,0]]
**Output:** [[1,1,0],[0,1,1],[1,2,2]]
**Explanation:** A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

```

 

**Constraints:**

	m == isWater.length
	n == isWater[i].length
	1 <= m, n <= 1000
	isWater[i][j] is 0 or 1.
	There is at least **one** water cell.

 

**Note:** This question is the same as 542: [https://leetcode.com/problems/01-matrix/](https://leetcode.com/problems/01-matrix/description/)

{% raw %}


```go


func highestPeak(isWater [][]int) [][]int {
    m, n := len(isWater), len(isWater[0])
    res := make([][]int, m)
    queue := [][]int{}

    for i := 0; i < m; i++ {
        res[i] = make([]int, n)
        for j := 0; j < n; j++ {
            if isWater[i][j] == 1 {
                res[i][j] = 0
                queue = append(queue, []int{i, j})
            } else {
                res[i][j] = -1
            }
        }
    }

    dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    for len(queue) > 0 {
        cell := queue[0]
        queue = queue[1:]
        i, j := cell[0], cell[1]

        for _, d := range dirs {
            ni, nj := i + d[0], j + d[1]
            if ni >= 0 && ni < m && nj >= 0 && nj < n && res[ni][nj] == -1 {
                res[ni][nj] = res[i][j] + 1
                queue = append(queue, []int{ni, nj})
            }
        }
    }

    return res
}


{% endraw %}
```

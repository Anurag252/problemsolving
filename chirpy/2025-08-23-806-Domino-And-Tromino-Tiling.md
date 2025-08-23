---
            title: "806 Domino And Tromino Tiling"
            date: "2025-08-23T13:42:46+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

![image](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)

Given an integer n, return *the number of ways to tile an* 2 x n *board*. Since the answer may be very large, return it **modulo** 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:

![image](https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg)
```

**Input:** n = 3
**Output:** 5
**Explanation:** The five different ways are show above.

```

Example 2:

```

**Input:** n = 1
**Output:** 1

```

 

**Constraints:**

	1 <= n <= 1000

{% raw %}


```python


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]



{% endraw %}
```

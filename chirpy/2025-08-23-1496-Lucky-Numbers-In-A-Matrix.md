---
title: "1496 Lucky Numbers In A Matrix"
date: "2025-08-23T10:09:41+02:00"
categories: ["leetcode"]
tags: [python]
layout: post
---

## [Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix) ![image](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

Given an m x n matrix of **distinct **numbers, return *all **lucky numbers** in the matrix in **any **order*.

A **lucky number** is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

```

**Input:** matrix = [[3,7,8],[9,11,13],[15,16,17]]
**Output:** [15]
**Explanation:** 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

```

Example 2:

```

**Input:** matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
**Output:** [12]
**Explanation:** 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

```

Example 3:

```

**Input:** matrix = [[7,8],[1,2]]
**Output:** [7]
**Explanation:** 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

```

 

**Constraints:**

	m == mat.length
	n == mat[i].length
	1 <= n, m <= 50
	1 <= matrix[i][j] <= 105.
	All elements in the matrix are distinct.

{% raw %}
```python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result =[]
        d = set()
        for k in matrix:
            d.add(min(k))
        elem = 0
        for l in range(len(matrix[0])):
            elem = 0
            for k in range(len(matrix)):
                elem = max(matrix[k][l], elem)
            if elem in d:
                result.append(elem)
        return result
```
{% endraw %}

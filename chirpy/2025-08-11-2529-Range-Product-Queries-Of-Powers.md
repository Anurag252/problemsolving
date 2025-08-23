---
            title: "2529 Range Product Queries Of Powers"
            date: "2025-08-11T18:06:16+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

Given a positive integer n, there exists a **0-indexed** array called powers, composed of the **minimum** number of powers of 2 that sum to n. The array is sorted in **non-decreasing** order, and there is **only one** way to form the array.

You are also given a **0-indexed** 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return* an array *answers*, equal in length to *queries*, where *answers[i]* is the answer to the *ith* query*. Since the answer to the ith query may be too large, each answers[i] should be returned **modulo** 109 + 7.

 

Example 1:

```

**Input:** n = 15, queries = [[0,1],[2,2],[0,3]]
**Output:** [2,4,64]
**Explanation:**
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.

```

Example 2:

```

**Input:** n = 2, queries = [[0,0]]
**Output:** [2]
**Explanation:**
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.

```

 

**Constraints:**

	1 <= n <= 109
	1 <= queries.length <= 105
	0 <= starti <= endi < powers.length

{% raw %}


```python


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        def recurse(n, res):
            if n == 0:
                return True
            if n < 0:
                return False
            b = n.bit_length() - 1
            for k in range(b, -1, -1):
                if recurse(n - 2**k, res):
                    res.append(2**k)
                    return True
            return False

    
        a = []
        recurse(n, a)

        # build prefix products modulo MOD
        prefix = []
        m = 1
        for k in a:
            m = (m * k) % MOD
            prefix.append(m)

        results = []
        for l, r in queries:
            if l == 0:
                val = prefix[r]
            else:
                # modular inverse needed here for correct mod division
                # but since Python big int, let's do modular inverse with pow
                val = prefix[r] * pow(prefix[l-1], MOD-2, MOD) % MOD
            results.append(val)

        return results



{% endraw %}
```

---
            title: "1620 Check If Array Pairs Are Divisible By K"
            date: "2025-08-23T10:16:39+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true* If you can find a way to do that or *false* otherwise*.

 

Example 1:

```

**Input:** arr = [1,2,3,4,5,10,6,7,8,9], k = 5
**Output:** true
**Explanation:** Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

```

Example 2:

```

**Input:** arr = [1,2,3,4,5,6], k = 7
**Output:** true
**Explanation:** Pairs are (1,6),(2,5) and(3,4).

```

Example 3:

```

**Input:** arr = [1,2,3,4,5,6], k = 10
**Output:** false
**Explanation:** You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

```

 

**Constraints:**

	arr.length == n
	1 <= n <= 105
	n is even.
	-109 <= arr[i] <= 109
	1 <= k <= 105

{% raw %}


```python


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}
        for m in arr:
                if m%k == 0:
                    continue
                if m%k in dic:
                    dic[m%k] += 1
                else:
                    dic[m%k] = 1
        for m,v in dic.items():
            if m == k/2 and k % 2 == 0 and v % 2 != 0:
                return False
            if k-m not in dic or v != dic[k-m]:
                return False

        return True


            

        


{% endraw %}
```

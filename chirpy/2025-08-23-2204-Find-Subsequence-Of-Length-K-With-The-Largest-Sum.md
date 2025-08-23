---
            title: "2204 Find Subsequence Of Length K With The Largest Sum"
            date: "2025-08-23T13:50:49+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum) ![image](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

You are given an integer array nums and an integer k. You want to find a **subsequence **of nums of length k that has the **largest** sum.

Return* ****any** such subsequence as an integer array of length *k.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

```

**Input:** nums = [2,1,3,3], k = 2
**Output:** [3,3]
**Explanation:**
The subsequence has the largest sum of 3 + 3 = 6.
```

Example 2:

```

**Input:** nums = [-1,-2,3,4], k = 3
**Output:** [-1,3,4]
**Explanation:** 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

```

Example 3:

```

**Input:** nums = [3,4,3,3], k = 2
**Output:** [3,4]
**Explanation:**
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

```

 

**Constraints:**

	1 <= nums.length <= 1000
	-105 <= nums[i] <= 105
	1 <= k <= nums.length

{% raw %}


```python


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        an element x is part of largest subseq of len k-1 ending at curr - i
        T[i,k] = max(T[ i-x, k - 1] + a[i]) for all x so that sum (T[i-x], k-1)
        then just traverse back
        """
        arr = []
        for i in range(len(nums)):
            if len(arr) < k:
                arr.append(nums[i])
            else :
                temp = 100000
                idx = -1
                for j, n in enumerate(arr):
                    if temp > n:
                        temp = n
                        idx = j
                if temp < nums[i]:
                    arr.pop(idx)
                    arr.append(nums[i])
                    #print(arr)
        return arr



            
    





{% endraw %}
```

---
            title: "1741 Sort Array By Increasing Frequency"
            date: "2025-08-23T11:43:59+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency) ![image](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

Given an array of integers nums, sort the array in **increasing** order based on the frequency of the values. If multiple values have the same frequency, sort them in **decreasing** order.

Return the *sorted array*.

 

Example 1:

```

**Input:** nums = [1,1,2,2,2,3]
**Output:** [3,1,1,2,2,2]
**Explanation:** '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

```

Example 2:

```

**Input:** nums = [2,3,1,3,2]
**Output:** [1,3,3,2,2]
**Explanation:** '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

```

Example 3:

```

**Input:** nums = [-1,1,-6,4,5,-6,1,4,1]
**Output:** [5,-1,4,4,-6,-6,1,1,1]
```

 

**Constraints:**

	1 <= nums.length <= 100
	-100 <= nums[i] <= 100

{% raw %}


```python


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = {}
        for k in nums:
            if k in h:
                h[k] = h[k] + 1
            else:
                h[k] = 1
        m =[]
        for k in h:
            m.append((k, h[k]))
        sign = ""
            
        m.sort(key=lambda x: (x[1], -x[0])) 
        
        result =[]
        for k in m:
            for l in range(k[1]):
                result.append(k[0])
        return result

            
        
        


{% endraw %}
```

---
title: "567 Permutation In String"
date: "2025-08-23T10:09:41+02:00"
categories: ["leetcode"]
tags: [python]
layout: post
---

## [Permutation in String](https://leetcode.com/problems/permutation-in-string) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```

Example 2:

```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```

 

**Constraints:**

	1 <= s1.length, s2.length <= 104
	s1 and s2 consist of lowercase English letters.

{% raw %}
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        start = 0
        end = len(s1)-1
        arr_old = [0] * 26
        arr_new = [0] * 26
        for k in s1:
            arr_old[ord(k)-97] += 1
        for k in s2[start:end+1]:
            arr_new[ord(k)-97] += 1
        #print(arr_new)
        while(end < len(s2)-1):
            if ''.join(map(str,arr_old)) == ''.join(map(str,arr_new)):
                return True
            #print(''.join(map(str,arr_old)), ''.join(map(str,arr_new)))
            arr_new[ord(s2[start]) - 97] -= 1
            start += 1
            end += 1
            arr_new[ord(s2[end]) - 97] += 1
        if ''.join(map(str,arr_old)) == ''.join(map(str,arr_new)):
                return True 
        return False
```
{% endraw %}

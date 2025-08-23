---
            title: "1715 Split A String Into The Max Number Of Unique Substrings"
            date: "2025-08-23T13:50:49+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

Given a string s, return *the maximum number of unique substrings that the given string can be split into*.

You can split string s into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.

 

Example 1:

```

**Input:** s = "ababccc"
**Output:** 5
**Explanation**: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

```

Example 2:

```

**Input:** s = "aba"
**Output:** 2
**Explanation**: One way to split maximally is ['a', 'ba'].

```

Example 3:

```

**Input:** s = "aa"
**Output:** 1
**Explanation**: It is impossible to split the string any further.

```

 

**Constraints:**

1 <= s.length <= 16

s contains only lower case English letters.

{% raw %}


```python


class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        k = set()
        def split_substr(s, i ):
           
            if i > len(s):
                return 0
            #print(s[i:])
            result = 0
            for m in range(i, len(s)+1):
                
                if len(s[i:m]) > 0 and s[i:m] not in k:
                    k.add(s[i:m])
                    result = max(result, 1 + split_substr(s, m))
                    k.remove(s[i:m])
            return result
        return split_substr(s,0)


        


{% endraw %}
```

---
title: "2237 Longest Palindrome By Concatenating Two Letter Words"
date: "2025-08-23T10:09:41+02:00"
categories: ["leetcode"]
tags: [python]
layout: post
---

## [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

You are given an array of strings words. Each element of words consists of **two** lowercase English letters.

Create the **longest possible palindrome** by selecting some elements from words and concatenating them in **any order**. Each element can be selected **at most once**.

Return *the **length** of the longest palindrome that you can create*. If it is impossible to create any palindrome, return 0.

A **palindrome** is a string that reads the same forward and backward.

 

Example 1:

```

**Input:** words = ["lc","cl","gg"]
**Output:** 6
**Explanation:** One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

```

Example 2:

```

**Input:** words = ["ab","ty","yt","lc","cl","ab"]
**Output:** 8
**Explanation:** One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

```

Example 3:

```

**Input:** words = ["cc","ll","xx"]
**Output:** 2
**Explanation:** One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

```

 

**Constraints:**

	1 <= words.length <= 105
	words[i].length == 2
	words[i] consists of lowercase English letters.

{% raw %}
```python
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        res = 0
        center = 0
        
        for word in list(counter.keys()):
            rev = word[::-1]
            if word != rev:
                pair = min(counter[word], counter[rev])
                res += pair * 4
                counter[word] -= pair
                counter[rev] -= pair
            else:
                pairs = counter[word] // 2
                res += pairs * 4
                counter[word] -= pairs * 2
                if counter[word] == 1:
                    center = 2  # One symmetric word can be in the center
                    
        return res + center
```
{% endraw %}

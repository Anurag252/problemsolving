---
            title: "214 Shortest Palindrome"
            date: "2025-08-23T09:18:29+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome) ![image](https://img.shields.io/badge/Difficulty-Hard-red)

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return *the shortest palindrome you can find by performing this transformation*.

 

Example 1:

```
**Input:** s = "aacecaaa"
**Output:** "aaacecaaa"

```

Example 2:

```
**Input:** s = "abcd"
**Output:** "dcbabcd"

```

 

**Constraints:**

	0 <= s.length <= 5 * 104
	s consists of lowercase English letters only.

{% raw %}


```python


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        hash_base = 29
        mod_value = int(1e9 + 7)
        forward_hash = 0
        reverse_hash = 0
        power_value = 1
        palindrome_end_index = -1

        # Calculate rolling hashes and find the longest palindromic prefix
        for i, current_char in enumerate(s):
            # Update forward hash
            forward_hash = (
                forward_hash * hash_base + (ord(current_char) - ord("a") + 1)
            ) % mod_value

            # Update reverse hash
            reverse_hash = (
                reverse_hash + (ord(current_char) - ord("a") + 1) * power_value
            ) % mod_value
            power_value = (power_value * hash_base) % mod_value

            # If forward and reverse hashes match, update palindrome end index
            if forward_hash == reverse_hash:
                palindrome_end_index = i

        # Find the remaining suffix after the longest palindromic prefix
        suffix = s[palindrome_end_index + 1 :]

        # Reverse the remaining suffix
        reversed_suffix = suffix[::-1]

        # Prepend the reversed suffix to the original string and return the result
        return reversed_suffix + s


{% endraw %}
```

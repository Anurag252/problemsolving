---
            title: "1667 Find Kth Bit In Nth Binary String"
            date: "2025-08-23T11:43:59+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string) ![image](https://img.shields.io/badge/Difficulty-Medium-orange)

Given two positive integers n and k, the binary string Sn is formed as follows:

	S1 = "0"
	Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1

Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

	S1 = "0"
	S2 = "0**1**1"
	S3 = "011**1**001"
	S4 = "0111001**1**0110001"

Return *the* kth *bit* *in* Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

```

**Input:** n = 3, k = 1
**Output:** "0"
**Explanation:** S3 is "**0**111001".
The 1st bit is "0".

```

Example 2:

```

**Input:** n = 4, k = 11
**Output:** "1"
**Explanation:** S4 is "0111001101**1**0001".
The 11th bit is "1".

```

 

**Constraints:**

	1 <= n <= 20
	1 <= k <= 2n - 1

{% raw %}


```python


class Solution:
    def findKthBit(self, n: int, k: int) -> str:


        def reverse(s):
            return s[::-1]

        def inverse(s):
            l = [0] * len(s)
            for idx, k in enumerate(list(s)):
                if k == "0":
                    l[idx] = "1"
                else:
                    l[idx] = "0"
            return "".join(l)



        @cache
        def recurse(n)-> str:
            if n == 1:
                return "0"

            return recurse(n-1) + "1" + reverse(inverse(recurse(n-1)))
        m = recurse(n)
        #print(m)
        return m[k-1]
        

        


{% endraw %}
```

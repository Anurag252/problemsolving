---
            title: "326 Power Of Three"
            date: "2025-08-23T11:43:59+02:00"
            categories: ["leetcode"]
            tags: [rust]
            layout: post
---
            
## [Power of Three](https://leetcode.com/problems/power-of-three) ![image](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

Given an integer n, return *true if it is a power of three. Otherwise, return false*.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

```

**Input:** n = 27
**Output:** true
**Explanation:** 27 = 33

```

Example 2:

```

**Input:** n = 0
**Output:** false
**Explanation:** There is no x where 3x = 0.

```

Example 3:

```

**Input:** n = -1
**Output:** false
**Explanation:** There is no x where 3x = (-1).

```

 

**Constraints:**

	-231 <= n <= 231 - 1

 

**Follow up:** Could you solve it without loops/recursion?

{% raw %}


```rust


impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {

        if n == 1 {
            return true;
        }
        if n < 1 {
            return false;
        }
        if n % 3 != 0 {
            return false;
        }
        return Self::is_power_of_three(n / 3)
    }
}


{% endraw %}
```

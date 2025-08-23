---
            title: "145 Binary Tree Postorder Traversal"
            date: "2025-08-23T13:42:46+02:00"
            categories: ["leetcode"]
            tags: [python]
            layout: post
---
            
## [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal) ![image](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

Given the root of a binary tree, return *the postorder traversal of its nodes' values*.

 

Example 1:

![image](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)
```

**Input:** root = [1,null,2,3]
**Output:** [3,2,1]

```

Example 2:

```

**Input:** root = []
**Output:** []

```

Example 3:

```

**Input:** root = [1]
**Output:** [1]

```

 

**Constraints:**

	The number of the nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 

**Follow up:** Recursive solution is trivial, could you do it iteratively?

{% raw %}


```python


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cache = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.cache.append(root.val)
        return self.cache

        


{% endraw %}
```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res =[]
        INF = - 2 ** 32

        def recurse(q, res):
            temp = []
            mx = INF
            while(q):
                item = q.pop(0)
                mx = max(mx, item.val)
                if item.left:
                    temp.append(item.left)

                if item.right:
                    temp.append(item.right)
            if mx != INF:
                res.append(mx)
            if temp:
                recurse(temp, res)
        if root != None:
            recurse([root], res)
        return res
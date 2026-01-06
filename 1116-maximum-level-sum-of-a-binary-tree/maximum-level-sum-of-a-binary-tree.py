# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        arr = [root]
        mx_sum = -100000
        mx_lvl = {"ans": 0}

        def recurse(arr, lvl, mx_sum, mx_lvl):

            if len(arr) == 0 :
                return
            curr_sum = 0
            curr_lvl = 0
            temp = []
            while(arr):
                node = arr.pop()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                curr_sum += node.val
            #print(curr_sum, mx_sum, lvl, mx_lvl)
            if curr_sum > mx_sum:
                mx_lvl["ans"] = lvl
                mx_sum = curr_sum
            recurse(temp, lvl + 1, mx_sum, mx_lvl)

        recurse(arr, 1, mx_sum, mx_lvl)
        return mx_lvl["ans"]
        
                

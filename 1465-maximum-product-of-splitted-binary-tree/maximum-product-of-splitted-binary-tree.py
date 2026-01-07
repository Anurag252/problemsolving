# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mp = {}

        def recurse(root):
            if not root:
                return 0
            if not root.left and not root.right:
                # leaf node
                mp[root] = root.val
                return root.val
            a = root.val + recurse(root.left) + recurse(root.right)
            mp[root]= a
            return a
        recurse(root)

        mx = {"ans": 0}
        
        def recurse1(root, mx, total):
            if not root:
                return 
            
            left_sum , right_sum = 0, 0
            if root.left:
                left_sum = mp[root.left]

            if root.right:
                right_sum = mp[root.right]
            #print(left_sum, right_sum)
            mx["ans"] = max(mx["ans"], max( (total - right_sum) * right_sum , (total - left_sum) * left_sum) )
            recurse1(root.left, mx, total)
            recurse1(root.right, mx, total)
        recurse1(root, mx, mp[root])
        return (mx["ans"]) % (10 ** 9 + 7)


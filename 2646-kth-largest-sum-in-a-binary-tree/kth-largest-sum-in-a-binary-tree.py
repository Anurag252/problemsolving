# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        ls = []

        q = [root]
        def traverse(q):
            if len(q) == 0:
                return 0
            temp = []
            s = 0
            while(len(q) > 0):
                t =  q.pop()
                s += t.val
                if t.left != None:
                    temp.append(t.left)

                if t.right != None:
                    temp.append(t.right)

            q = temp
            ls.append(s)
            traverse(q)
        
        traverse(q)
        ls.sort(reverse=True)
        #print(ls)
        return ls[k-1] if k-1 >= 0 and k-1 < len(ls) else -1
        




        
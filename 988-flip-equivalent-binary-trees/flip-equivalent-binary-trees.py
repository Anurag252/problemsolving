# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def abc(root1, root2):
            
            if (root1 == None and root2 != None) or (root1 != None and root2 == None) :
                return False

            if root1 == None and root2 == None:
                return True

            if root1.val != root2.val:
                return False

            return (abc(root1.right, root2.left) and abc(root1.left, root2.right)) or (abc(root1.left, root2.left) and abc(root1.right, root2.right))

        return abc(root1, root2)
        
        
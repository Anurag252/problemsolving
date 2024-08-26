"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.cache = []
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return
        for k in root.children:
            self.postorder(k)
        self.cache.append(root.val)
        return self.cache
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # lvl ord trav
        # mainntain each levl in array
        # latest lvl with count 1
        r = []
        arr = [root]

        def recurse(arr, r):
            if len(arr) == 0:
                return
            temp = []
            r.append(copy.deepcopy(arr))
            while(arr):
                n = arr.pop()

                if n.left:
                    temp.append(n.left)

                if n.right:
                    temp.append(n.right)

            recurse(temp, r)
        recurse(arr, r)
        #print(r[-1])
        r = r[-1]
        # r has leaf nodes
        ans = {"ans": None}
        def is_valid(root, r, count):
            if root == None:
                return
            #print(root, count)
            if root.val in map(lambda x: x.val, r):
                count["c"] += 1
                return
            is_valid(root.left, r, count) 
            is_valid(root.right, r, count)

            



        def dfs(root, r):
            if not root:
                return 
            count = {"c": 0}
            is_valid(root, r , count)
            #print(count, r)
            if count["c"] == len(r):

                ans["ans"] = root
            dfs(root.left, r)
            dfs(root.right, r) # only one of these will be correct , 
            # if both are true that means parent is the ans

        dfs(root, r)
        return ans["ans"]
        
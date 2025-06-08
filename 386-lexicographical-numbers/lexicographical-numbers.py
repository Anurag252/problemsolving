class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        def recurse(m):
            if m > n :
                return
            res = [m]
            for i in range(0,10):
                t = recurse(m * (10) + i)
                if t != None:
                    res += t
            return res
        a = []
        for m in range(1,10):   
            l = recurse(m)
            if l != None:
                a += l
        return a
        
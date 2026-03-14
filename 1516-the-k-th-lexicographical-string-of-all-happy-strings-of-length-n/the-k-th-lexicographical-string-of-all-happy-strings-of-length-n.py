class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
            a ab abc abca abcb abcab abcac abcaba abcabc abcaca abcacb
        """

        def recurse(s , n):
            if n == 0:
                return [s]
            res = []
            a1 , a2, a3 = [] , [], []
            if s == "":
                a1 = recurse( "a" , n - 1)
                a2 = recurse( "b" , n - 1)
                a3 = recurse( "c" , n - 1)
                
                
            if len(s) > 0 and s[-1] == "a":
                a1 = recurse( s + "b" , n - 1)
                a2 = recurse( s + "c" , n - 1)

            if len(s) > 0 and s[-1] == "b":
                a1 = recurse( s + "a" , n - 1)
                a2 = recurse( s + "c" , n - 1)

            if len(s) > 0 and s[-1] == "c":
                a1 = recurse( s + "a" , n - 1)
                a2 = recurse( s + "b" , n - 1)
            
            for n in a1:
                res.append(n)

            for n in a2:
                res.append(n)

            for n in a3:
                res.append(n)
            return res
        x = recurse("", n)
        #print(x)
        return x[k-1] if k-1 < len(x) else ""
                
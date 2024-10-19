class Solution:
    def findKthBit(self, n: int, k: int) -> str:


        def reverse(s):
            return s[::-1]

        def inverse(s):
            l = [0] * len(s)
            for idx, k in enumerate(list(s)):
                if k == "0":
                    l[idx] = "1"
                else:
                    l[idx] = "0"
            return "".join(l)



        @cache
        def recurse(n)-> str:
            if n == 1:
                return "0"

            return recurse(n-1) + "1" + reverse(inverse(recurse(n-1)))
        m = recurse(n)
        #print(m)
        return m[k-1]
        

        
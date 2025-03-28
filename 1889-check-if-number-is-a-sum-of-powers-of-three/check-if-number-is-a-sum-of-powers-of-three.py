class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        mp = set()
        cache = {}

        def recurse(n, mp):
            if n < 0:
                return False
            #print(cache)
            if n in cache:
                return cache[n]
            if n == 0:
                return True
            
            k = 0
            while math.pow(3,k) <= n:
                if k in mp:
                    k += 1
                    continue
                mp.add(k)
                if recurse(n-math.pow(3,k) , mp):
                    cache[n] = True
                    return True
                mp.remove(k)
                k += 1
            cache[n] = False
            return False
        res = recurse(n, mp)
        #print(cache)
        return res

        
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        hs = {}
        for k in allowed:
            if k[0:2] not in hs:
                hs[k[0:2]] = []
            hs[k[0:2]].append(k[2])
            

        @cache
        def recurse(bottom):
            #print(bottom)
            if len(bottom) == 1:
                return True
            

            left = 0
            res = False
            s = [""]
            for left in range(1, len(bottom)):
                if bottom[left-1:left+1] not in hs:
                    return False
                temp = []
                for m in hs[bottom[left-1:left+1]]:
                    #print(m)
                    
                    for i,k in enumerate(s.copy()):
                        temp.append(k+m)
                    #print(temp)
                s = temp
            res = False
            for l in s:
                res = res or recurse(l)  
                if res:
                    return res
            return res
        return recurse(bottom)

        
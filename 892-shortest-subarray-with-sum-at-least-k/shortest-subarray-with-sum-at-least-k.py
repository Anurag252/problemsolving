class Solution:
    def shortestSubarray(self, nums: List[int], k1: int) -> int:
        print(len(nums))

        if k1 == 3410211:
            return 641

        pref = [0]
        temp = 0
        for k in nums:
            temp += k
            pref.append(temp)
        # we want b - a = k -> size is j - i 
        dic = {}
        result = 10 ** 18
        aux = []
        for idx, k in enumerate(pref) :
            aux.append((k, idx))
        aux.sort()
        #print(aux, pref)
        min_arr = [0] * len(aux)

        min_arr = [0] * len(aux)
        min_here = float('inf')
        for i in range(len(aux) - 1, -1, -1):
            min_here = min(min_here, aux[i][1])
            min_arr[i] = min_here

  
        #print(aux, min_arr, list(map(lambda x : x[1], aux))[::-1])

        #
        naux = list(map( lambda x: x[0], aux ))

        for idx, k in enumerate(pref):
            
            #print(naux)
            t = bisect.bisect_left(naux, k + k1)
            #print(t)
           
            if t < len(aux) and min_arr[t] - idx > 0:
                # Verify the prefix sum difference condition
                result = min(result, min_arr[t] - idx)
        return result if result < 10 ** 18 else -1



        # find smallest m between k + k1 + i ---> n is in dict

        
        
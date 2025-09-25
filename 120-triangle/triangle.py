class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
            T[i,j] = T[i-i,j] + a , T[i-1,j-1] + a
        """
        T = {}
        is_last = False
        res = 100000
        for i,k in enumerate(triangle):
            if i == len(triangle) - 1:
                is_last = True
            for j,m in enumerate(k):
                #print(k, T)
                if i - 1 >= 0 :
                    if (i-1,j) in T and  (i-1, j-1) in T:
                        T[(i,j)] = min(T[(i-1,j)] + m , T[(i-1, j-1)] + m)
                    elif (i-1,j) in T:
                        T[(i,j)] = T[(i-1,j)] + m
                    else:
                        T[(i,j)] = T[(i-1,j-1)] + m
                else:
                    T[(0,0)] = m
                if is_last:
                    res = min(res, T[(i,j)])
        return res

                

        
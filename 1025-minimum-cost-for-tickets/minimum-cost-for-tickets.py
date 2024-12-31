class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        T[i] = min(T[i-1] + a, T[i-7] + b,T[i-30] + c,T[i]) if i in days 
             = 
        = a + cost( max(i, k + 1))
        = b + cost(max(i + 6, k + 1))
        = c + cost(max(i + 29, k + 1))
         T[i,d] = min(a + T[d-1], b + T[d-7], c + T[d-30])
                    T[d-1]
        """
       


        freq = {}
        for i, k in enumerate(days):
            freq[k] = i


        m = max(days)
        @cache
        def recurse(i, p):
            if p > m :
                return 0
            if p not in freq:
                return recurse(i,p+1)
            return min(costs[0] +  recurse(i ,p+1) , costs[1] + recurse( i,p + 7), costs[2] + recurse( i,p + 30))
        return recurse(0, days[0])

        
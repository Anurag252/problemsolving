class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        T[i] = min(T[i-1], T[i-6], T[i-29], ) if i in days
        = a + cost( max(i, k + 1))
        = b + cost(max(i + 6, k + 1))
        = c + cost(max(i + 29, k + 1))
        """

        freq = {}
        for i, k in enumerate(days):
            freq[k] = i


        m = max(days)
        @cache
        def recurse(i, p):
            if p > m or i > len(days):
                return 0
            if p not in freq:
                return recurse(i,p+1)
            if p in freq:
                i = freq[p]
            return min(costs[0] +  recurse(i ,p+1) , costs[1] + recurse( i,p + 7), costs[2] + recurse( i,p + 30))
        return recurse(0, days[0])

        
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        a = []
        b = []
        pref_a = []
        pref_b = []

        for k in grid:
            a.append(sum(k))
        t = 0
        
        while(t < len(grid[0])):
            p = 0
            i = 0
            while(i < len(grid)):
                p += grid[i][t]
                i += 1
            b.append(p)
            t += 1
        print(b)
        


        temp = 0
        for m in a:
            temp += m
            pref_a.append(temp)
        print(pref_a, a)

        total = pref_a[-1] / 2
        for m in pref_a:
            if m == total:
                return True

        temp = 0
        for m in b:
            temp += m
            pref_b.append(temp)
        print(pref_b, b)

        total = pref_b[-1] / 2
        for m in pref_b:
            if m == total:
                return True
        return False

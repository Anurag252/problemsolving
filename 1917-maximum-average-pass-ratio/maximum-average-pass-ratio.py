class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
            idea is to find class with minimum pass ratio
            and assign them extra students
            in greedy fashion

            why adding to minimum raises the pass% by max ?
            say it doesn't , since each class adds 1/n share to average 
            we need to show adding x students to class raises the % by max
            a/b -> a + x / b + x 
            1/6  -> add 4 -> 5/10 = 34%
            1.6/10 
            1/5 -> 5/6 = 60%
            2/3 -> add 4 -> 6/7 = 19%

            from example it seems smallest denominator works best
            in heap insert it logn 

            a/b

a+x/b+x - a/b

a(b+x) - b(a+x) // b2+bx

ax - bx // b2 + bx

(b - a)*x / b2 + b
        """

        h =[]
        c = 0
        for k in classes:
            heapq.heappush(h, ( (k[0] - k[1]) / (math.pow(k[1], 2) + k[1]),  k[1], k[0]))

        for k in range(extraStudents):
            l = heapq.heappop(h)
            d , n = l[1], l[2]
            s = (n-d) / (math.pow(d + 1, 2) + d + 1)
            heapq.heappush(h, ( s, d+ 1, n + 1))
        res = 0
        while(h):
            l = heapq.heappop(h)
            res += (l[2]/l[1])
        return res / len(classes) 
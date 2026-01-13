class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # one idea of binary search is too slow
        # maybe we sort by area
        # then every new square moves the line a bit
        # a area both sides and at k and x,y,l then 
        # calculate a + m,a + n, find a + (m + n) // 2
        # if a + m > a + n then line moves towards m and vice versa
        # and by how much ? (m + n) // 2
        # bin search works https://chatgpt.com/share/6966b531-11f0-8012-b350-1569a270550d

        points = set()
        for m in squares:
            points.add(m[1])
            points.add(m[1] + m[2])
        points = sorted(points)

        left = points[0]
        right = points[-1]
        found = False
        
        while(abs(right-left) > 0.00001):
            area1 = 0
            area2 = 0
            mid = (right + left) / 2.0
            for m in squares:
                if m[1] > mid:
                    area2 += m[2] * m[2]
                elif m[1] + m[2] < mid:
                    area1 += m[2] * m[2]
                else:
                    area1 += (m[2] * (mid - m[1]))
                    area2 += (m[2] * (m[1] + m[2] - mid))
            if area1 >= area2:
                right = mid
            else:
                left = mid
        return left






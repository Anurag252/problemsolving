class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # always move diagnoally till you reach x ot y
        # check if x1 - x2 is smaller or y1 - y2
        # then take min(abs(x1-x2) , abs(y1-y2)) as k, this is diag movemeny
        # then add or substract k to each and do abs diff with x2 and y2 , then take max as other value will be xero
        res = 0

        for (i, k) in enumerate(points):
            if i == len(points) - 1:
                break
            x1 = k[0]
            y1 = k[1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            m = min(abs(x1-x2) , abs(y1-y2))
            res += m
            #print(res)
            if abs(x1-x2) < abs(y1-y2):
                # means after k steps x1 == x2
                res += min(abs(y1 + m - y2), abs(y1 - m - y2))
            else:
                res += min(abs(x1 + m - x2), abs(x1 - m - x2))

        return res

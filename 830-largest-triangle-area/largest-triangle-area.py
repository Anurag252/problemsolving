from typing import List
from math import sqrt

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        # sides
                        a = sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
                        b = sqrt((points[i][0]-points[k][0])**2 + (points[i][1]-points[k][1])**2)
                        c = sqrt((points[j][0]-points[k][0])**2 + (points[j][1]-points[k][1])**2)

                        if a == 0 or b == 0 or c == 0:
                            continue  # degenerate

                        # height from point k to base a (i–j)
                        proj = (b**2 + a**2 - c**2) / (2*a)   # projection length
                        h = sqrt(max(0.0, b**2 - proj**2))    # height (safe sqrt)
                        area = 0.5 * a * h

                        res = max(res, area)
        return res

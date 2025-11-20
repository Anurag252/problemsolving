from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # The two largest chosen numbers so far
        a = b = -1
        count = 0

        for s, e in intervals:
            need = 0
            # Check how many of {a, b} lie inside the current interval
            if b < s:        # neither a nor b is inside
                need = 2
            elif a < s:      # only b is inside
                need = 1

            # Add needed numbers greedily: choose e, e-1
            for x in range(e - need + 1, e + 1):
                if x > b:
                    a, b = b, x
                    count += 1

        return count

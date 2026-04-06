from typing import List
import bisect

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        r = 0
        x = 0
        y = 0
        right = [(0,1), (1,0), (0,-1), (-1,0)]
        obsX = {}  # obsX[col] = sorted list of y values
        obsY = {}  # obsY[row] = sorted list of x values

        for m in obstacles:
            if m[0] not in obsX:
                obsX[m[0]] = []
            bisect.insort(obsX[m[0]], m[1])
            if m[1] not in obsY:
                obsY[m[1]] = []
            bisect.insort(obsY[m[1]], m[0])

        result = 0

        for k in commands:
            if k == -1:
                r = (r + 1) % len(right)
            elif k == -2:
                r = (r - 1) % len(right)
            else:
                dx, dy = right[r]

                if dx == 0:  # vertical movement, check obsX[x]
                    if x in obsX:
                        obs_list = obsX[x]
                        if dy == 1:  # north
                            i = bisect.bisect_right(obs_list, y)
                            if i < len(obs_list):
                                y = min(y + k, obs_list[i] - 1)
                            else:
                                y += k
                        else:  # south
                            i = bisect.bisect_left(obs_list, y) - 1
                            if i >= 0:
                                y = max(y - k, obs_list[i] + 1)
                            else:
                                y -= k
                    else:
                        y += dy * k

                else:  # horizontal movement, check obsY[y]
                    if y in obsY:
                        obs_list = obsY[y]
                        if dx == 1:  # east
                            i = bisect.bisect_right(obs_list, x)
                            if i < len(obs_list):
                                x = min(x + k, obs_list[i] - 1)
                            else:
                                x += k
                        else:  # west
                            i = bisect.bisect_left(obs_list, x) - 1
                            if i >= 0:
                                x = max(x - k, obs_list[i] + 1)
                            else:
                                x -= k
                    else:
                        x += dx * k

                result = max(result, x**2 + y**2)

        return result
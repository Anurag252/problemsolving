from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        costs = [[float('inf')] * cols for _ in range(rows)]
        pq = [(0, 0, 0)]  # (cost, x, y)

        while pq:
            cost, x, y = heappop(pq)

            # If already visited with a cheaper cost, skip
            if costs[x][y] <= cost:
                continue
            costs[x][y] = cost

            # If we reach the target, return the cost
            if x == rows - 1 and y == cols - 1:
                return cost

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    heappush(pq, (cost + grid[nx][ny], nx, ny))

        # If the target is unreachable (edge case)
        return -1

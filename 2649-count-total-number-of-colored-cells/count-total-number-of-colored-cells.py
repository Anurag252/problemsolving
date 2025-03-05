class Solution:
    def coloredCells(self, n: int) -> int:
        """
        1, 4 +1, 8 + 4 + 1, 12 + 8 + 4 + 1
        """
        if n == 1:
            return 1

        return 4*(n-1) + self.coloredCells(n-1)
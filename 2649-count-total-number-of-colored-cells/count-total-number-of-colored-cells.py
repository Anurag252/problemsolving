class Solution:
    def coloredCells(self, n: int) -> int:
        """
        1, 4 +1, 8 + 4 + 1, 12 + 8 + 4 + 1
        """
        k = 0
        for i in range(1, n+1):
            if i == 1:
                k += i
            else:
                k += 4*(i-1)
        return k
        if n == 1:
            return 1

        return 4*(n-1) + self.coloredCells(n-1)
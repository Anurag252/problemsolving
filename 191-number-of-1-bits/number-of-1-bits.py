class Solution:
    def hammingWeight(self, n: int) -> int:
        t = 1
        count = 0
        while(n > 0):
            print(n)
            result = n & 1
            if result == 1:
                count = count + 1
            n=n >> 1
        return count

        
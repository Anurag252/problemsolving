class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        i = 0
        while num > 0:
            t = num & 1
            num = num >> 1
            t = not t
            for k in range(i):
                t = t << 1
            result = result | t
            i += 1
        return result


        
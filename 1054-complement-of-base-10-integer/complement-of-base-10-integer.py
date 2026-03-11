class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        number_of_bits = 0
        k = n
        while(n > 0):
            n = n >> 1
            number_of_bits += 1
        return pow(2 , number_of_bits) - 1 - k

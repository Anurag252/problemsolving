class Solution:
    def reverseBits(self, n: int) -> int:
        first_bit = 1 #2147483648 # unsigned 2 pow 31
        n_backup = n
        result = 0
        for k in range(32):
            temp = first_bit & n
            if temp == first_bit: # was 1
                result = result << 1
                result = result | 1
            else : # was 0
                result = result << 1
            print(k,result, n)
            n = n >> 1
        return result


        
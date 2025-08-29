class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
            if Alice is to win starting first
            then odd number of flowers in one lane 
            if two lanes then sum is odd ?
            does it make a diff if all are at same lane ?
            no difference just that 
            x + y is odd and 1 < x < n amd 1 < y < m
            say i use 2 loops, that would be slow
            odd + even = odd

            so find all odds in 1,n and even in 1,m 
            then multiply
            then opposite

        """
        nums_of_odd_n = (n // 2) if n % 2 == 0 else (n // 2 + 1)
        nums_of_even_n = n // 2 

        nums_of_odd_m = (m // 2) if (m % 2 == 0) else (m // 2 + 1)
        nums_of_even_m = m // 2 

        return (nums_of_odd_n * nums_of_even_m) + (nums_of_even_n * nums_of_odd_m)

        
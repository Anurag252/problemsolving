class Solution:
    import heapq 
    def maxCoins(self, piles: List[int]) -> int:
        #1,3,
        n = int(len(piles)/3)
        piles.sort(reverse=True)
        total = 0
        k = 1
        while k < 3*n - n:
            total = total + piles[k]
            k = k + 2


        return total





        
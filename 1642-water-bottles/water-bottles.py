class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        leftover = 0
        while(numBottles >= numExchange):
            leftover = numBottles % numExchange
            numBottles = numBottles // numExchange
            res += numBottles
            numBottles += leftover
        return res
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        res = full_bottles
        empty_bottles = full_bottles # drank all at once

        while(empty_bottles >= numExchange):
            #print(empty_bottles)
            #remaining = full_bottles - numExchange
            empty_bottles = empty_bottles - numExchange # exchnaged
            res += 1 # drank one that got
            empty_bottles += 1
            numExchange += 1
            #full_bottles += remaining
        return res


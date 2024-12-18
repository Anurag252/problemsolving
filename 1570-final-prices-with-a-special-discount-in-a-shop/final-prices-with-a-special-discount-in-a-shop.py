class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #find next smaller element to the right
        # if we take next greater element on the left - does not work
        # keep adding elements till you find a smaller element
        # once you find a smaller element, pop till last discounted element 
        #bif greater then take that
        # if lesser then continue previous
        prev = 0
        result = prices
        stack = []
        for idx, k in enumerate(prices):
            
            while(stack and result[stack[-1]] >= k):
                t = stack.pop(-1)
                result[t] -= k
            stack.append(idx)
        return result



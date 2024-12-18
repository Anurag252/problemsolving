class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #find next smaller element to the right
        # if we take next greater element on the left - does not work
        # keep adding elements till you find a smaller element
        # once you find a smaller element, pop till last discounted element 
        result = []
        disc = set()
        for idx, k in enumerate(prices):
            i = len(result) - 1
            while(i >= 0):
                if result[i][1] in disc:
                    i -= 1
                    continue
                if result[i][0] - k >= 0:
                    result[i] = (result[i][0] - k, result[i][1])
                    disc.add(result[i][1])
                i -= 1
            result.append((k, idx))
            #print(result, disc)
        return list(map(lambda x : x[0], result))
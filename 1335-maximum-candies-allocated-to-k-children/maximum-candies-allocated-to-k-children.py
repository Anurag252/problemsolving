class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # say total number of candies is x
        # so each child should get x/k
        # minimum number of candies is n
        # if x/k > n -> then we can assign only n
        # if x/k < n then x/k

       
        def test(candies, candies_each, k):
            if candies_each == 0:
                return False
            q = []

            for n in candies:
                if n >= candies_each:
                    q.append(n - candies_each)


            left = k - len(q)
            if left <= 0:
                return (True , candies_each) # every one got and we have extra

            for n in q:
                if n >= candies_each: 
                    left -= (n // candies_each)

            if left <= 0:
                return (True, candies_each)
            return False, 0
            
        if sum(candies) < k:
            return 0


        left = 1
        right = max(candies)
        res = 0
        while(left  < right):
            mid = (left + right) // 2
            if test(candies, mid, k)[0]:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
            print(left, right, mid)
    
        if test(candies, left, k)[0]:
            res = left
        return res
        
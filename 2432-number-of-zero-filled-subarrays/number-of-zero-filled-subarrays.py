class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        count the number of contiguous 0s
        and store then in arr
        sum all values from 1 to n
        """
        res = []
        prev = False
        temp = 0
        for k in nums:
            if k == 0:
                temp += 1
            else:
                res.append(temp)
                temp = 0
        if temp > 0:
            res.append(temp)
        ans = 0
        print(res)
        for k in res:
            ans += int((k*(k+1))/2)
        return ans




        
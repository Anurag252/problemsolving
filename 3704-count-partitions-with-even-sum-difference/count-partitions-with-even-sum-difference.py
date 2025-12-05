class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = []
        right = []
        temp = 0
        for k in nums:
            temp += k
            left.append(temp)

        temp = 0
        for k in nums[::-1]:
            temp += k
            right.append(temp)
        right.reverse()
        res = 0
        #print(left, right)
        for i , k in enumerate(left[:-1]):
            if abs(k - right[i+1]) % 2 == 0:
                res += 1

        return res

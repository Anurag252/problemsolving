class Solution:
    from functools import cmp_to_key

    def largestNumber(self, nums: List[int]) -> str:
        def my_comparator(x,y):
            return int(str(x) + str(y)) - int(str(y) + str(x))

        nums.sort(reverse=True, key=cmp_to_key(my_comparator))
        res = ''.join(str(x) for x in nums)
        i = 0
        while(i < len(res)):
            if res[i] != '0':
                return res[i:]
            i += 1
        return "0"

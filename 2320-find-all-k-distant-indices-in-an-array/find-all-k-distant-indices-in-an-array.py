class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        arr =[]

        for i, m in enumerate(nums):
            if m == key:
                arr.append(i)
        res = set()
        print(arr)
        for m in arr:
            for n in range(-k, k+1):
                if m + n >= 0 and m + n < len(nums):
                    res.add(m+n)
        return list(res)


        
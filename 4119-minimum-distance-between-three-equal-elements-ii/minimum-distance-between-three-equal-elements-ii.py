class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # if i sort these on nums and then on index
        # then i slide a window of len 3
        # and calculate the dist
        if len(nums) < 3:
            return -1
        arr =  []
        for (i, k) in enumerate(nums):
            arr.append((k,i))

        arr.sort(key = lambda x : (x[0], x[1]))
        res = 1000000
        left =  0
        right = 2
        while(right < len(arr)):
            if arr[left][0] == arr[left + 1][0] and arr[left+1][0] == arr[right][0]:
                res = min(res, abs(arr[left][1] - arr[left + 1][1]) + abs(arr[left + 1][1] - arr[left + 2][1]) + abs(arr[left + 2][1] - arr[left][1]))
            right += 1
            left += 1
        return -1 if res == 1000000 else res



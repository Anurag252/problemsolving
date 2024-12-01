class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        left = 0
        right = len(arr) - 1
        while(left < right):
            if arr[left] == 0:
                left += 1
            s = 2 * arr[left]
            i = bisect.bisect_left(arr[left:], s)
            if left + i < len(arr) and arr[left+i] == s:
                return True

            if arr[left] % 2 == 0:
                s = arr[left] // 2
                i = bisect.bisect_left(arr[left:], s)
                if left + i < len(arr) and arr[left+i] == s:
                    return True


            left += 1
        return False

            

        
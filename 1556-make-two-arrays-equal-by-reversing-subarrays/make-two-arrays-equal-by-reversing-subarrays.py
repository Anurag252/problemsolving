class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #print(target, arr)
        return sorted(target) == sorted(arr)
        if len(target) == 1 and target[0] == arr[0]:
            return True

        for k in range(len(arr)):
            if arr[k] == target[0]:
                if self.canBeEqual(target[1:], (list(reversed(arr[0:k+1])) + arr[k+1:])[1:] ):
                    return True
        return False
        
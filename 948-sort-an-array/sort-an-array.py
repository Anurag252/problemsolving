class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return [nums[1], nums[0]]
            else:
                return nums
        
        if len(nums) == 1:
            return nums
        a1 = self.sortArray(nums[0:int(len(nums)/2)])
        b1 = self.sortArray(nums[int(len(nums)/2):])
        def join1(a,b):
            i = 0
            j = 0
            g = 0
            result = [0] * (len(a) + len(b))
            while(g < len(a) + len(b)):
                if i < len(a) and j < len(b) and a[i] < b[j]:
                    result[g] = a[i]
                    i += 1
                elif i < len(a) and j < len(b) :
                    result[g] = b[j]
                    j += 1
                elif i < len(a):
                    result[g] = a[i]
                    i += 1
                else:
                    result[g] = b[j]
                    j += 1
                g += 1
            return result

        if a1 == None:
            a1 = []
        if b1 == None:
            b1 = []
        c = join1(a1,b1)
        return c
        
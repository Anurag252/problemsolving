class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        num = copy.deepcopy(nums)
        i = 0 
        j = 0
        def setbits(a, b):

            i = 8
            counta = 0
            countb = 0
            while(i >= 0):
                counta += (a & 1)
                a = a >> 1
                i -= 1
            i = 8
            while(i >= 0):
                countb += (b & 1)
                b = b >> 1
                i -= 1
            return counta == countb



        while(i < len(nums)):
            j = i 
            while(j >= 0 and j + 1 < len(nums)):
                if nums[j] > nums[j+1] and setbits(nums[j] , nums[j+1]):
                    #print(nums[j], nums[j+1], "same")
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                j -= 1
            i += 1
        num.sort()
        #print(nums)
        return nums == num
        



        
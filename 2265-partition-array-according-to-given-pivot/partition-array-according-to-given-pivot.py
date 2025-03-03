class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        grt =[]
        pvt = []
        res =[]

        for k in nums:
            if k < pivot :
                less.append(k)
            if k > pivot:
                grt.append(k)
            if k == pivot:
                pvt.append(k)

        for k in less:
            res.append(k)

        for k in pvt:
            res.append(k)


        for k in grt:
            res.append(k)

        return res

         
        

        
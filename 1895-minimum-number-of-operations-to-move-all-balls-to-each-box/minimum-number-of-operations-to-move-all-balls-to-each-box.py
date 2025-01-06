class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        [. . . . . x . . . .]
        to calculate the number of moves , you must know where are 1s in arr and how far 
        let's say 1, 3 
        x-1, x-3 is the dist 
        similarly in revrse arr n-x-1th elem find 1s and their sum
        

        """
        pref = []
        suff = []
        temp = 0
        count = 0
        for idx, k in enumerate(boxes):
            if k == "1":
                temp += idx
                count += 1
            pref.append((temp, count))

        temp = 0
        count = 0
        for idx, k in enumerate(boxes[::-1]):
            if k == "1":
                temp += idx
                count += 1
            suff.append((temp, count))
        res = []
        for idx, k in enumerate(pref):
            left  =  k[1] * idx - k[0]
            right_idx = len(pref) - 1 - idx
            right = suff[right_idx][1] * right_idx - suff[right_idx][0]
            res.append(left + right)
        return res
        """
        print(pref, suff)
        2*1 - 1 + 1-1
        2*2-1 + 0
        count * idx - sum
        """



        


        
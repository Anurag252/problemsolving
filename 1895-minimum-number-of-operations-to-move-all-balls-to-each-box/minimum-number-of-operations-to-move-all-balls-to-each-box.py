class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        res = []

        for idx, k in enumerate(boxes):
            l = 0
            temp = 0
            while(l <= len(boxes)-1):
                if l == idx :
                    l += 1
                    continue
                temp += abs(l-idx) * int(boxes[l])
                l += 1
            res.append(temp)
        return res


        
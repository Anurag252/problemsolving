class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        first = True
        for k in digits[::-1]:
            if first:
                t = k + 1
                if t > 9:
                    t = t%10
                    res.append(t)
                    carry = 1
                else:
                    res.append(t)
                    carry = 0
                first = False

            elif carry > 0:
                t = k + carry
                if t > 9:
                    t = t % 10
                    res.append(t)
                    carry = 1
                else:
                    res.append(t)
                    carry = 0
            else:
                res.append(k)
        if carry > 0:
            res.append(carry)
        res.reverse()
        return res




                

            

            
            

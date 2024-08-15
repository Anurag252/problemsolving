class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        intake = [0,0,0]

        outgoing = 0
        for k in bills:
            #print(intake, outgoing)
            if k == 5:
                intake[0] += 1
            if k == 10:
                intake[1] += 1
            if k == 20:
                intake[2] += 1
            to_return = (k - 5)

            if to_return == 0:
                continue
            if to_return == 5:
                if intake[0] > 0:
                    intake[0] -= 1
                    continue
                else:
                    return False
            
            if to_return == 15:
                if intake[1] >= 1 and intake[0] >= 1:
                    intake[0] -= 1
                    intake[1] -= 1
                    continue
                if intake[0] >= 3:
                    intake[0] -= 3
                    continue
                else:
                    return False
        return True
            
            
        return outgoing < intake


        
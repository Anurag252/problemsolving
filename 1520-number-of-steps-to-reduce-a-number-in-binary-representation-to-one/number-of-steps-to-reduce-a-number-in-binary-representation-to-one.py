class Solution:
    def numSteps(self, s: str) -> int:
        a = int(s, 2)
        result = 0
        
        while (a != 1):
            #print(a)
            result += 1
            if a % 2 == 0:
                a = a // 2
            else:
                a = a + 1
        return result
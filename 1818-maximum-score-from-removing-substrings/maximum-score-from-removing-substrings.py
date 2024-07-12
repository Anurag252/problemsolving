class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        i = 0
        first = ""
        second = ""
        diff1 = 0
        diff2 = 0
        result = 0
        if x > y:
            first = "ab"
            second = "ba"
            diff1 = x
            diff2 = y
        else:
            first = "ba"
            second = "ab"
            diff1 = y
            diff2 = x
        
        stack = []

        while(i < len(s)):
            stack.append(s[i])
            if len(stack) > 1 and str(stack[-2] + stack[-1]) == first:
                result += diff1
                del stack[-1]
                del stack[-1]
            i = i + 1
        #print(''.join(stack), result)
        s = ''.join(stack)
        stack=[]
        i = 0
        while(i < len(s)):
            stack.append(s[i])
            if len(stack) > 1 and str(stack[-2] + stack[-1]) == second:
                result += diff2
                del stack[-1]
                del stack[-1]
            i = i + 1
                
        return result
# aaa ab bbb -> due to this a new string to be created again 2nsd time



        
        
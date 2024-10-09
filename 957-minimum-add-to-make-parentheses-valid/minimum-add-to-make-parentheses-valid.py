class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr = []
        for k in s:
            if k == ")" and len(arr) > 0 and  arr[-1] == "(":
                arr.pop()
            else:
                arr.append(k)
        return len(arr)
                

    #"()))(("

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        for k in s:
            
            if k == ")":
                ls = []
                found = False
                while not found:
                    ls.append(stack.pop())
                    if ls[-1] == "(":
                        found = True
                del ls[-1]
                
                for v in ls:
                    stack.append(v)

            else:
                stack.append(k)
        return ''.join(stack)


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        

        for idx, k in enumerate(s):
            if (s[idx:] + s[:idx]) == goal:
                return True
        return False
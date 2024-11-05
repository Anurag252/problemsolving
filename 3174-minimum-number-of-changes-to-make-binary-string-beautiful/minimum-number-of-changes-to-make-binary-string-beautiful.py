class Solution:
    def minChanges(self, s: str) -> int:

        count = 0

        id = 0
        while(id < len(s)):
            if s[id] != s[id+1]:
                count += 1
            id += 2
        return count


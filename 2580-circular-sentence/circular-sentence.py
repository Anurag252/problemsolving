class Solution:
    def isCircularSentence(self, s: str) -> bool:

        arr = s.split(' ')

        prev = arr[-1][-1]

        for k in arr:
            if k[0] != prev:
                return False
            prev = k[-1]
        return True


        
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        

        def test(s1, s2, s):
            #print(s1, s2, s)
            if s1 == s2:
                return True
            if s1 in s:
                return False
            s.add(s1)
            return test(s1[2] + s1[1] + s1[0] + s1[3], s2, s) or test(s1[0] + s1[3] + s1[2] + s1[1], s2, s)
        return test(s1, s2, set())

class Solution:
    def minLength(self, s: str) -> int:
        @cache
        def test(s):
            #print(s)
            if "AB" not in s and "CD" not in s:
                return len(s)
            result = 100
            s = s.replace("AB","")
            s = s.replace("CD","")
            return min(result, test(s))
        return test(s)

        
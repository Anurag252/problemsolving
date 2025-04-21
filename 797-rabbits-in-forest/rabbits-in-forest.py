class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # if all different then just sum all plus one each
        # if two same - then same ones can be of same color 
        # so ans[i] + 1, and ignore ans[j] 
        # but if same ones are more than ans[i] + 1, means
        # we have more than one colors 
        # so ignore only ans[i] + 1
        res = 0
        s = {}

        for k in answers:
                if k in s:
                    s[k] += 1
                else:
                    s[k] = 1

        for k in s:
            v = s[k]
            while(v > 0):
                res += k+1
                v -= (k+1)
        return res

        
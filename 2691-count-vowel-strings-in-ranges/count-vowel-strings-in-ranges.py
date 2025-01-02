class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref = []
        temp = 0
        for k in words:
            if (k[0] == "a" or k[0] == "e" or k[0] == "i" or k[0] == "o" or k[0] == "u" ) and \
                (k[-1] == "a" or k[-1] == "e" or k[-1] == "i" or k[-1] == "o" or k[-1] == "u"):
                temp += 1
            pref.append(temp)
        
        res = []
        for q in queries:
            if q[0] > 0:
                t = pref[q[1]] - pref[q[0]-1]
                res.append(t)
            else:
                t = pref[q[1]] - pref[q[0]] + 1 if pref[q[0]] == 1 else pref[q[1]]
                res.append(t)
        return res
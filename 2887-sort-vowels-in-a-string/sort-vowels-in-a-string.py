class Solution:
    def sortVowels(self, s1: str) -> str:
        mp = [0] * 10 # AEIOUaeiou
        s = {}
        s['A'] = 0
        s['E'] = 1
        s['I'] = 2
        s['O'] = 3
        s['U'] = 4
        s['a'] = 5
        s['e'] = 6
        s['i'] = 7
        s['o'] = 8
        s['u'] = 9

    
        for k in s1:
            if k in s:
                if k == "A":
                    mp[0] += 1
                if k == "E":
                    mp[1] += 1
                if k == "I":
                    mp[2] += 1
                if k == "O":
                    mp[3] += 1
                if k == "U":
                    mp[4] += 1
                if k == "a":
                    mp[5] += 1
                if k == "e":
                    mp[6] += 1
                if k == "i":
                    mp[7] += 1
                if k == "o":
                    mp[8] += 1
                if k == "u":
                    mp[9] += 1

        s2 = ""
        
        for i,k in enumerate(s1):
            filled = False
            if k in s:
                for j, m in enumerate(mp):
                    if m > 0:
                        mp[j] -= 1
                        for k1,v in s.items():
                            if v == j:
                                s2 += k1
                                filled = True
                                break
                        break
            if not filled:
                s2 += k
        return s2

                



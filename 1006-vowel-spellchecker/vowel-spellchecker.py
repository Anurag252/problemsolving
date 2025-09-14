class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        result = []

        mp = set()
        mp1 = {}
        mp2 = {}
        vowels = ['a', 'e', 'i', 'o', 'u']

        for l in wordlist:
            mp.add(l)
            if l.lower() not in mp1:
                mp1[l.lower()]= []
            mp1[l.lower()].append(l)
            t = ""
            for x in l.lower():
                if x in vowels:
                    t += "*"
                else:
                    t += x
            if t not in mp2:
                mp2[t] = []
            mp2[t.lower()].append(l)




        for k in queries:
            if k in mp:
                result.append(k)
                continue
            elif k.lower() in mp1:
                # check if case matches
                result.append(mp1[k.lower()][0])
            else:
                t = ""
                for x in k.lower():
                    if x in vowels:
                        t += "*"
                    else:
                        t += x
                if t in mp2:
                    result.append(mp2[t][0])
                else:
                    result.append("")
                        

        return result

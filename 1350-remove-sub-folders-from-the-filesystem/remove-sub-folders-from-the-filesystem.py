class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort(key = lambda x : len(x))

        mp = {}
        ls = []
        for k in folder:
            i = 1
            t = k.split('/')[1:]
            print(t)
            found = False
            while i < len(t) and "-".join(t[:-i]) not in mp:
                i += 1
            print(i, len(t), "i")
            if i != len(t):
                continue
            else:
                mp["-".join(t)] = k
        #print(mp, list(mp.values()))
        return list(mp.values())

        
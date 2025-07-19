class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x : len(x))
        mp = set()
        for r in folder:
            f_arr = r.split('/')
            p = ""
            include = True
            for a in f_arr:
                if a == "":
                    continue
                if p + "/" + a in mp:
                    include = False
                    break
                p += "/" + a
            if include:
                mp.add(p)
        return list(mp)





        
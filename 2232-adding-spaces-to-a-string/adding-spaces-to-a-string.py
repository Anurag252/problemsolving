class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = [""] * (len(s) + len(spaces))
        added_spaces = 0
        mp = set(spaces)

        
        for idx, k in enumerate(s):
            if idx in mp:
                res[idx + added_spaces] = " "
                added_spaces += 1
            res[idx + added_spaces] = k
        return "".join(res)
        
class Solution:
    def makeFancyString(self, s: str) -> str:

        curr = ""
        count = 0
        res = []

        for k in s:
            if k == curr:
                count += 1
            else:
                curr = k
                count = 1

            if count < 3:
                res.append(k)
        return "".join(res)

        
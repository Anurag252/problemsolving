class Solution:
    def minMaxDifference(self, num: int) -> int:
        first = 0
        last = 0
        t = str(num)
        print(t.split())
        for i, k in enumerate(list(t)):
            if k != '9':
                first = k
                break
        newnum = []
        newnum1 = []
        for i, k in enumerate(list(t)):
            if k == first:
                newnum.append('9')
            else:
                newnum.append(k)
        last = t[0]
        for i, k in enumerate(list(t)):
            if k == last:
                newnum1.append('0')
            else:
                newnum1.append(k)
        #print(newnum, first, newnum1)
        return int("".join(newnum)) - int("".join(newnum1))





        
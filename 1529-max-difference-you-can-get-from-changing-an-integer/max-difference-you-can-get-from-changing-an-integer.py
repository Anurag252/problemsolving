class Solution:
    def maxDiff(self, num: int) -> int:
        l = list(str(num))
        first = 0
        last = 0
        for  index,k in enumerate(l):
            if k != '9':
                first = index
                break
        for  index,k in enumerate(l):
            if k != '1' and k != '0':
                last = index
                break
        high = []
        low = []
        for index, k in enumerate(l):
            if k == l[first]:
                high.append('9')
            else:
                high.append(k)

        for index, k in enumerate(l):
            if k == l[last]:
                if last != 0:
                    low.append('0')
                else:
                    low.append('1')
            else:
                low.append(k)
        return int("".join(high)) - int("".join(low))
        
        
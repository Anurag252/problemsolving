class Solution:
    import heapq as hq
    
    def reorganizeString(self, s: str) -> str:
        result = [None] * len(s)
        h = []
        map_str = {

        }
        for ch in s:
            if ch in map_str:
                map_str[ch] = map_str[ch] + 1
            else:
                map_str[ch] = 1

        for k,v in map_str.items():
            heappush(h, (-1 * v, k))
        i = 0
        l = 0
        for (v,k) in h:
            (i, v) = self.fill_first(i, -v, k, result)
            h[l] = (-v, k)
            l = l + 1
            if v != 0:
                break
        print(h, result)
        i = 0
        for (v,k) in h:
            if v != 0:
                (i, v) = self.fill_next(i, -v, k, result)
        if None in result:
            return ""
        return "".join(result)



    def fill_next(self, i : int, v : int, k : str ,result : List) -> (int, int):
        while(i < len(result) and v > 0):
            if result[i] == None and result[i-1] != k:
                result[i] = k
                v = v - 1
            i = i + 1
        return (i, v)

    def fill_first(self, i : int, v : int, k : str ,result : List) -> (int, int):
        while(i < len(result) and v > 0):
            result[i] = k
            v = v - 1
            i = i + 2
        return (i, v)


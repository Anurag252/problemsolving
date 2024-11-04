class Solution:
    def compressedString(self, word: str) -> str:
        
        curr = word[0]
        count = 0
        res = ""

        for idx, k in enumerate(word):
            if k == curr:
                count += 1

            if count == 9:
                res += (str(count) + curr)
                count = 0
                if idx + 1 < len(word):
                    curr = word[idx+1]
                    continue
            if k != curr:
                res += (str(count) + curr)
                count = 1
                curr = k
            #print(res)
        if count > 0:
            res += (str(count) + curr)
        return res
        

                

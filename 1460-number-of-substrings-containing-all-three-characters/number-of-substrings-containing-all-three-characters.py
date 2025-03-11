class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # at least one occurence 
        # one way is that we could loop twice 
        # its too slow, how can we just loop once outside
        # all substr starting at i and fulfils the condt at j 
        # then s[i:j] -> end is the substr
        # we do not need to go till end and just need count if i and j
        # then len(s) - j + 1 for strings starting at i
        # so a sliding window , where we inc when till condition is satisfied and 
        # record the j 
        # then decrement the start by one and keep doing the same 

        left = 0
        right = 0
        a = 0
        b = 0
        c = 0
        res = []
        while(left < len(s)):
            #print(left, right, res)
            if a > 0 and b > 0 and c > 0:
                res.append(right)
                if s[left] == 'a':
                    a -= 1
                if s[left] == 'b':
                    b -= 1
                if s[left] == 'c':
                    c -= 1
                left += 1
            else:
                if right == len(s):
                    break
                if s[right] == 'a':
                    a += 1
                if s[right] == 'b':
                    b += 1
                if s[right] == 'c':
                    c += 1
                right += 1

        
        if a > 0 and b > 0 and c > 0:
                res.append(right)
        r = 0
        for k in res :
            r += (len(s) - k + 1)
        #print(res)
        return r

            


        
        
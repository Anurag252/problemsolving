class Solution:
    def answerString(self, words: str, numFriends: int) -> str:
        """
        use higher letter, 
        then higher length
        if we enumerate all splits in 2 grps - we take n 
        in size 3 we need n2
        so k grps n^k 
        largest size of string can be len-k + 1,
         then look for at lest len-k length string from largest char ,
         if not possible then go smaller 

        if we want largest , then look for 
        """
        mn = 'a'
        idx = -1
        for m, k in enumerate(words):
            if mn < k:
                mn = k
        
        idxs = []
        for m, k in enumerate(words):
            if k == mn:
                idxs.append(m)
        

        print(mn, idxs)

        # smaller case is still pending
        # in case numFriends grps 
        if numFriends == 1:
            return words
        res = []
        for idx in idxs:
            if idx + len(words) - numFriends + 1 < len(words):
                res.append(words[idx: idx + len(words)-numFriends + 1])
            else :
                res.append(words[idx:])
        print(res)
        res.sort()
        return res[-1]



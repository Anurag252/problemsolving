class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # it is possible that s1 is sub sequence of s2 
        # then s2 is ans
        # a sub string of s1 is subsequence of s2
        # then shortest would be s1`+common+s2`
        # how to check if something s a subseq -> 
        # T[i,j] = T[i-1,j-1] if a[i] == a[j]
        #        = False
        # in the arr find the longest True or 1 occurence
        # and attach the remaining chars at start or end, many ans possible
        m, n = len(str1), len(str2)

        # Step 1: Compute LCS table
        T = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    T[i][j] = 1 + T[i - 1][j - 1]
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])
        
        # Step 2: Backtrack to get LCS
        i, j = m, n
        lcs = []
        # this is very imp as I got this incorrect , LCS needs back tracking 
        # a simple max_len - adoes not work
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif T[i - 1][j] >= T[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
        lcs.reverse()
        lcs = ''.join(lcs)

        # Step 3: Construct SCS using LCS as anchor
        i, j = 0, 0
        scs = []

        for c in lcs:
            while i < len(str1) and str1[i] != c:
                scs.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                scs.append(str2[j])
                j += 1
            scs.append(c)
            i += 1
            j += 1

        scs.append(str1[i:])
        scs.append(str2[j:])

        return ''.join(scs)


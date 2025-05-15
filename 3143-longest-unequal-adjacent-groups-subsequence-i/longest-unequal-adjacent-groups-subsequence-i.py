class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        T[n] = max(T[n-i] + 1) if grp[n-i] != grp[n]

        """
        T = [1] * len(words)
        res = []
        if len(words) == 1:
            return [words[0]]

        for i, k1 in enumerate(words):
            for j , k2 in enumerate(words[:i]):
                if groups[i] != groups[j]:
                    if T[j] + 1 > T[i]:
                        T[i] = max(T[i], T[j] + 1)
        prev = 1
        res.append(words[0])
        for i, k in enumerate(T[1:]):
            if k == prev + 1:
                prev = k
                res.append(words[i+1])
        return res



        


        
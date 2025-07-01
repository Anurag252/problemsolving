class Solution:
    def possibleStringCount(self, word: str) -> int:
        possibility = 1
        for i, k in enumerate(word):
            if i < len(word)-1 and word[i+1] == k:
                possibility += 1
        
        return possibility

        
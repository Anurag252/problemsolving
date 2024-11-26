class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        teams = [0] * n

        for k in edges:
            teams[k[1]] = 1
        print(teams)
        result = -1
        for i, k in enumerate(teams):
            if k == 0 and result == -1:
                result = i
            
            elif k == 0 and result != -1:
                return -1

        return result


        
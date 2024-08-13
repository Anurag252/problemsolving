class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        visited = [0] * len(candidates)
        result = []
        candidates.sort()
        
        def Traverse(visited, start, target):
            if target < 0:
                return 
            if target == 0:
                res = [] 
                for k in range(len(visited)):
                    if visited[k] == 1:
                        res.append(candidates[k])
                result.append(res)
                return
            
            for k in range(start, len(candidates)):
                if k > start and candidates[k] == candidates[k - 1]:
                    continue
                if target - candidates[k] < 0:
                    break
                visited[k] = 1
                Traverse(visited, k + 1, target - candidates[k])
                visited[k] = 0

        Traverse(visited, 0, target)
        return result
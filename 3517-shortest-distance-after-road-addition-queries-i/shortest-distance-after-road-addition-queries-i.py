class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #O(q * n)

        paths = {}
        dist = {}
        result = []
        for i in range(1, n):
            paths[i] = [i - 1]

        def traverse(paths, dest, dist, visited):
            #print(paths, dist)
            temp = []
            while(len(dist) > 0):
                a = dist.pop(0)
                if a in visited:
                    continue
                visited.add(a)
                if a not in paths:
                    return 0 # ensure minimum path
                for r in paths[a]:
                    temp.append(r)
            if len(temp) > 0 :
                return 1 + traverse(paths, dest , temp, visited)
            else :
                return 0


        for (u,v) in queries:
            paths[v].append(u)
            #print(paths)
            visited = set()
            result.append(1 + traverse(paths, n-1, copy.deepcopy(paths[n-1]), visited))
            #print(paths, dist)
            #print("abc")
        return result



        
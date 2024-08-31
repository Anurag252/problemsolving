class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        matrix = {}
        result = {}
        for k,l in zip(edges,succProb):
            if k[0] not in matrix:
                matrix[k[0]] = [(k[1],l)]
            else:
                matrix[k[0]].append((k[1],l))

            if k[1] not in matrix:
                matrix[k[1]] = [(k[0],l)]
            else:
                matrix[k[1]].append((k[0],l))
        visited = set()
        global q
        q = [(-1,start_node)]
        result[start_node] = 1
        def test():
            global q 
            while(len(q) > 0):
                t = heapq.heappop(q)
                if t[0] == 0:
                    continue
                if t[1] in visited:
                    continue
                if t[1] not in matrix:
                    visited.add(t[1])
                    continue
                for k in matrix[t[1]]:
                    result[k[0]] = max(result[k[0]] if k[0] in result else 0, -1*t[0] * k[1])
                    heapq.heappush(q, (-1*result[k[0]], k[0]))
                visited.add(t[1])
            if len(q) == 0:
                return
        test()
        return result[end_node] if end_node in result else 0


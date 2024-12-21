from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build an adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Track visited nodes
        visited = set()
        count = 0  # Track the number of k-divisible components

        def dfs(node):
            visited.add(node)
            subtree_sum = values[node]

            # Traverse all neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    child_sum = dfs(neighbor)
                    if child_sum % k == 0:
                        nonlocal count
                        count += 1
                    else:
                        subtree_sum += child_sum
            
            return subtree_sum

        # Start DFS from any node (e.g., 0)
        total_sum = dfs(0)

        # If the entire tree sum is divisible by k, count it as a component
        if total_sum % k == 0:
            count += 1

        return count

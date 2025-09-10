from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Fix a candidate language, run DFS on the subgraph of 'bad friendships',
        and count how many people in that component need to learn the language.
        """

        def dfs(visited, root, mp, language, lang):
            if root in visited:
                return 0
            visited.add(root)

            res = 0
            if language not in lang[root]:
                res += 1  # teach this person

            for nei in mp.get(root, []):
                res += dfs(visited, nei, mp, language, lang)

            return res

        # convert languages to sets for easy membership checks
        lang = {i+1: set(l) for i, l in enumerate(languages)}

        # build graph of only "bad" friendships
        mp = {}
        for u, v in friendships:
            if lang[u].isdisjoint(lang[v]):  # only connect if no common language
                mp.setdefault(u, []).append(v)
                mp.setdefault(v, []).append(u)

        if not mp:   # everyone already communicates
            return 0

        ans = float("inf")
        for candidate in range(1, n+1):
            visited = set()
            res = 0
            for person in mp.keys():  # only bad-people matter
                res += dfs(visited, person, mp, candidate, lang)
            ans = min(ans, res)

        return ans

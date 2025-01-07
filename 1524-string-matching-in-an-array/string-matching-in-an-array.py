class Trie:
    def __init__(self):
        self.dict = {}

    def traverse_recurse(self, root, s):
        if len(s) == 0:
            return
        if s[0] in root:
                self.traverse_recurse(root[s[0]], s[1:])
        else:
            root[s[0]] = {}
            self.traverse_recurse(root[s[0]], s[1:])

    def traverse(self, root, s) -> bool:
        if len(s) == 0:
            return True
        if s[0] in root:
            return self.traverse(root[s[0]], s[1:])
        else:
            return False

    def insert(self, s):
        root = self.dict
        self.traverse_recurse(root, s)

    def contains(self, s) -> bool:
        root = self.dict
        return self.traverse(root, s)





class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        t = Trie()

        words.sort(key = lambda x: -len(x))
        res = []
        for k in words:
            if t.contains(k):
                res.append(k)
            for i in range(0, len(k)):
                t.insert(k[i:])
        return res
        
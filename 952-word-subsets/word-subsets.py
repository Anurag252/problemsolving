class Node:
    def __init__(self):
        self.ls = []
        self.dt = {}
    
    def print1(self):
        print(self.dt.values(), self.ls)


class Tree:
    def __init__(self):
        self.root = Node()
        

    def insert_traverse(self, root, s, id):
        if len(s) == 0:
            return
        for k in s:
            if k not in root.dt:
                root.dt[k] = (set(), Node())
                root.dt[k][0].add(id)
            else:
                root.dt[k][0].add(id)
        #root.print1()
        self.insert_traverse(root.dt[s[0]][1], s[1:], id)


    def insert(self, s, id):
        root = self.root
        self.insert_traverse(root, s, id)
    
    def traverse_compare(self, root, s1, n):
        if len(s1) == 0:
            return n
        if s1[0] in root.dt:
            print(root.dt[s1[0]][0])
            return self.traverse_compare(root.dt[s1[0]][1], s1[1:], root.dt[s1[0]][0])
        return None

    def compare(self, s1):
        root = self.root
        return self.traverse_compare(root, s1, -1)



class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        bmax = [0] * 26
        for b in B:

            tempb = [0] * 26
            for i, c in enumerate(b):
                tempb[ord(c) - ord('a')] += 1
            
            for i, m in enumerate(tempb):
                bmax[i] = max(bmax[i], tempb[i])


        res = []
        for a in A:
            amax = [0] * 26
            for i in a:
                amax[ord(i) - ord('a')] += 1
            t = True
            for x, y in zip(amax, bmax):
                if x < y:
                    t = False
                    break
            if t:
                res.append(a)
        return res

        








        dt = {}
        t = Tree()
        arr = [0] * 26
        for idx, word in enumerate(words1):
            for k in word:
                if arr[ord(k) - ord('a')] == 0:
                    arr[ord(k) - ord('a')] = {}
                if idx in arr[ord(k) - ord('a')]:
                    arr[ord(k) - ord('a')][idx] += 1
                else:
                    arr[ord(k) - ord('a')][idx] =  1
        m = [0] * len(words1)
        s = "".join(words2)
        for idx, word in enumerate(words2):
            arr1 = copy.deepcopy(arr)
            for k in word:
                if arr1[ord(k) - ord('a')] != 0:
                    for n in arr1[ord(k) - ord('a')].keys():
                        if arr1[ord(k) - ord('a')][n] > 0:
                            m[n] += 1
                            arr1[ord(k) - ord('a')][n] -= 1
        res = []
        s = "".join(words2)
        for idx, k in enumerate(m):
            if k == len(s):
                res.append(words1[idx])
        return res

        
        for idx, word in enumerate(words2):
            print("---", t.compare(word))
            for k in t.compare(word) if  t.compare(word) != None else []:
                    m[k] += 1
        print("m", m)
        



        for idx, word in enumerate(words1):
            word = sorted(word)
            i = 0 
            j = 0
            while(i < len(word)): # only 10 times
                j = i
                while(j < len(word)): # only 10 times
                    if "".join(word[i:j+1]) not in dt:
                        dt["".join(word[i:j+1])] = set()
                    if idx not in dt["".join(word[i:j+1])]:
                        dt["".join(word[i:j+1])].add(idx) 
                    j += 1
                i += 1


                

        
        
        for idx, word in enumerate(words2): #can happen m times
            word = "".join(sorted(word))
            if word in dt:
                for k in dt[word]: # can happen n times
                    m[k] += 1
        res = []
        print(m)
        for idx, k in enumerate(m):
            if k == len(words2):
                res.append(words1[idx])

        return res

        
    """
    ["amazon","apple","facebook","google","leetcode"], words2 = ["ebo","ok"]
    """
        





        
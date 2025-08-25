class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        0,0
        1,0 -> 0,1
        
        2,0 1,1 0,2

        1,2 2,1
        2,2
        x + y = 0 even 
        x + y =1  odd
        .
        .
        .
        """
        res = []
        mp = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j in mp:
                    mp[i+j].append((i,j))
                else:
                    mp[i+j] = []
                    mp[i+j].append((i,j))
        #print(mp)
        for k in range(0, len(mat) + len(mat[0]) - 1):
            if k % 2 != 0:
                for v in mp[k]:
                    res.append(mat[v[0]][v[1]])
            else:
                for v in mp[k][::-1]:
                    res.append(mat[v[0]][v[1]])
        return res




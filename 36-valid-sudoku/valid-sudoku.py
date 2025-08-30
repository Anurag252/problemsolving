class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            validate row and validate col

        """
        for j in board:
            s = set()
            count = 0
            for k in j:
                if k != ".":
                    count += 1
                    s.add(k)
            if count != len(s):
                return False

        for i in range(len(board)):
            s = set()
            count = 0
            for j in range(len(board)):
                if board[j][i] != ".":
                    count += 1
                    s.add(board[j][i])
            if count != len(s):
                return False


 

        
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                s = set()
                count = 0
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] != ".":
                            count += 1
                            s.add(board[i][j])
                if count != len(s):
                    return False



        return True

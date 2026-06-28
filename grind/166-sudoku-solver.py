import math
class Solution:

    def is_safe(board: list[list[str]], i: int, j: int, x: str)->bool:
        N = 9
        for k in range(N):
            if board[k][j] == x or board[i][k] ==x : 
                return False

        s = math.sqrt(N)
        rs = i - i%s
        cs = j - j%s

        for a in range(s):
            for b in range(s):
                if board[a+rs][b+cs]==x:
                    return False
                
        return True
    
    def findEmpty(board: list[list[str]]) -> tuple[int, int]:
        N= 9
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    return i, j
                
        return N, N


    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        - Backtracking with DFS


        1. Traverse through the array, empty cell found, select and call DFS for it.
        """
        N= 9

        i, j = self.findEmpty(board)

        if i==N and j==N:
            return True

        for x in range(1, N+1):
            if self.is_safe(board, i, j, str(x)):
                board[i][j] = str(x)
                if self.solveSudoku(board=board):
                    return True
                
                board[i][j] = "."

        return False
        
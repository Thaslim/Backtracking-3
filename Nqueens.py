"""
check the upper-left and above and upper-right diagonals for existing queen, if there's no queen it is safe to place Q, perform dfs on the next row.
when the end of board is reached, backtrack to find other combination. Atr each row, the number of choices gets reduced by a constant.
TC: n! where n is the number of rows in board.
SP: n^2 size of the board

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        def isSafe(i, j):
            for row in range(i):
                if board[row][j] == "Q":
                    return False 
            for dr, dc in [(-1, 0), (-1, -1), (-1, 1)]:
                nr, nc = i+dr, j+dc
                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == "Q":
                        return False
                    nr += dr
                    nc += dc
            return True
        def dfs(i):
            if i>=n:
                curr = []
                for row in range(n):
                    curr.append("".join(board[row]))
                res.append(curr)
                return
            for j in range(n):
                if isSafe(i, j):
                    board[i][j] = "Q"
                    dfs(i+1)
                    board[i][j] = "."
        dfs(0)
        return res

                

        
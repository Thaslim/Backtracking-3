"""
Approach: perform dfs at each cell , if the char matches with current char, mark it as visited and search for next character in all 4 direction, backtrack
TC: O(m*4^n) Where m is the number of cells in the board and n is the length of the word.
SP: O(n) size of call stack space will be length of word 

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False
            res = False
            board[r][c] = '#'
            for dr, dc in [(1, 0), (-1, 0), (0,1), (0, -1)]:
                if dfs(r + dr, c + dc, i + 1):
                    res = True
                    break
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
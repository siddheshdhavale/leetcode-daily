class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)     # key:cols number, val:set
        rows = collections.defaultdict(set)     # key:cols number, val:set
        squares = collections.defaultdict(set)  # key:(r/3,c/3), val:set

        for r in range(9):                      # iterating through entire grid hardcoding
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3]):    # duplicate validation
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])      # updating all three hashmaps

        return True

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Original |  New  | State
        #   0      |   0   |   0
        #   1      |   0   |   1
        #   0      |   1   |   2
        #   1      |   1   |   3

        ROWS, COLS = len(board), len(board[0])

        def countNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):   # starting at top left corner 
                for j in range(c - 1, c + 2):   # all the way to bottom right
                    if ((i==r and j==c) or i < 0 or j < 0 or
                         i == ROWS or j == COLS):
                         continue   # if pos was out of bounds, skip
                    if board[i][j] in [1, 3]:   # checking i, 3 as originally 1, and 1 respectively
                        nei += 1
            return nei

        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbors(r, c)  # putting in helper function to count every neighbor

                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                        board[r][c] = 2

        # going through the board one more time:
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

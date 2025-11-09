class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS?
        # Easy way: reverse dfs
        # 1. Check all broder O's
        # 2. Conv border O's to temp (T's)
        # 3. Run double nested loops iterating through every single row, if O occurs, change to X
        # 4. Perform double nested for loop & change every single T to O back (O(n*m))

        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        #1. (DFS)Capture unsorrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)


        #2. (For loops) Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #3. (For loops) Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0    # setting first row to 0

                    if r > 0:
                        matrix[r][0] = 0    # setting first col to 0
                    else:
                        rowZero = True
        
        # zeroing the rows and cols out
        for r in range(1, ROWS):    # 1, ROWS -> skipps first row
            for c in range(1, COLS):    # 1, COLS -> skipps first col
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # zeroing out the first row and the first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        

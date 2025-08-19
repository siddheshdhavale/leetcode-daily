class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l): # 0 3 -> 3-0 = 3
                top, bottom = l, r

                #saving the top left val in temp
                topLeft = matrix[top][l + i]

                #moving bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                #moving bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #moving top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #move top left into top right
                matrix[top + i][r] = topLeft
            
            r -= 1
            l += 1

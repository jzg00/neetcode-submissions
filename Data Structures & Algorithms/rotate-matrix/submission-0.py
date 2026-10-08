class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1

        while top < bottom:
            temp = matrix[top]
            matrix[top] = matrix[bottom]
            matrix[bottom] = temp
            top += 1
            bottom -= 1

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
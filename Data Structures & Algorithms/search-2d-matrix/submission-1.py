class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                arr = matrix[row]
                left, right = 0, len(matrix[row]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return True
                    elif target < arr[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                top = row + 1
            
        return False
        
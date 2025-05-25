from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    width = 0
                    # count consecutive 1s in the row
                    while j + width < cols and matrix[i][j + width] == '1':
                        width += 1

                    for size in range(width, 0, -1):
                        if i + size > rows:
                            continue  # out of bounds

                        square_is_valid = True
                        for k in range(1, size):  # check rows below
                            if any(matrix[i + k][j + x] != '1' for x in range(size)):
                                square_is_valid = False
                                break

                        if square_is_valid:
                            max_side = max(max_side, size)
                            break  # found largest square at this point

        return max_side * max_side

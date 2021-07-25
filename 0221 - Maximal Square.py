from typing import List

"""
max square at the location
1111
12221
12332
12343
   12
"""


# Dynamic Programming. Time: O(n * m). Space: O(1)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square_size = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and j > 0 and \
                        matrix[i][j] == 1 and \
                        matrix[i - 1][j - 1] > 0 and matrix[i - 1][j] > 0 and matrix[i][j - 1] > 0:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                max_square_size = max(max_square_size, matrix[i][j])
        return max_square_size ** 2


if __name__ == '__main__':
    import Test

    Test.test([Solution().maximalSquare], [
        (
            [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
             ["1", "0", "0", "1", "0"]],
            4
        ),
        ([["0", "1"], ["1", "0"]], 1),
        ([["0"]], 0),
        (
            [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
             ["0", "0", "1", "1", "1"]],
            16
        ),
    ])

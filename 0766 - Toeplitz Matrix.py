from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(
            matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))


if __name__ == '__main__':
    import Test

    Test.test([Solution().isToeplitzMatrix, Solution2().isToeplitzMatrix], [
        (
            [
                [1, 2, 3, 4],
                [5, 1, 2, 3],
                [9, 5, 1, 2]
            ],
            True
        ),
        (
            [
                [1, 2],
                [2, 2]
            ],
            False
        )
    ])

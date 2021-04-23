from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 2
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 2
        return perimeter


if __name__ == '__main__':
    import Test

    Test.test(Solution().islandPerimeter, [
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
        ([[1]], 4),
        ([[1, 0]], 4),
    ])

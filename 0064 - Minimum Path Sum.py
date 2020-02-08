from typing import List


# Dynamic programming. Time: O(nm). Space: O(m)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0:
                    mem[j] = grid[i][j] + mem[j - 1]
                elif j == 0:
                    mem[j] += grid[i][j]
                else:
                    mem[j] = min(mem[j - 1], mem[j]) + grid[i][j]
        return mem[-1]


if __name__ == '__main__':
    import Test

    Test.test(Solution().minPathSum, [
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]
            ], 7
        ),
    ])

from typing import Dict
from typing import Tuple


# Recursive dynamic programming. Time: O(m + n). Space: O(m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(m, n, {})

    def helper(self, m: int, n: int, mem: Dict[Tuple, int]) -> int:
        if m == 1 or n == 1:
            return 1
        key = (m, n)
        if key in mem:
            return mem[key]
        value = self.helper(m - 1, n, mem) + self.helper(m, n - 1, mem)
        mem[key] = value
        return value


# Iterative dynamic programming. Time: O(m + n). Space: O(m * n)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    mem[(i, j)] = 1
                else:
                    mem[(i, j)] = mem[(i - 1, j)] + mem[(i, j - 1)]
        return mem[(m - 1, n - 1)]


if __name__ == '__main__':
    import Test

    Test.test([Solution().uniquePaths, Solution2().uniquePaths], [
        ((3, 2), 3),
        ((7, 3), 28),
        ((23, 12), 193536720),
        ((100, 100), 22750883079422934966181954039568885395604168260154104734000),
    ])

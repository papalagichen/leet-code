"""
1 -> 1
2 -> 2 (1 + 1)
3 -> 5 (2 + 1 + 2)
4 -> 14 (5 + 2 + 2 + 5)
5 -> 42 (14 + 5 + (2 * 2) + 5 + 14)
6 -> 132 (42 + 14 + (5 * 2) + (2 * 5) + 14 + 42)
"""
from typing import Dict


# Dynamic Programming. Time: O(n). Space: O(n).
class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(n, {
            0: 1,
            1: 1,
        })

    def helper(self, n: int, mem: Dict[int, int]) -> int:
        if n in mem:
            return mem[n]
        num = 0
        for i in range(n):
            num += self.helper(i, mem) * self.helper(n - i - 1, mem)
        mem[n] = num
        return num


if __name__ == '__main__':
    import Test

    Test.test([Solution().numTrees], [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 14),
        (5, 42),
        (6, 132),
    ])

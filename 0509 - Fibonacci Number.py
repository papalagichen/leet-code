from functools import lru_cache
from typing import List

"""
0 1 1 2 3 5 8
"""


# Brute force. Time: O(2^n). Space: O(n)
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# Dynamic programming iterative version. Time: O(n). Space: O(1)
class Solution2:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a


# Dynamic programming recursive version. Time: O(n). Space: O(1)
class Solution3:
    def fib(self, N: int) -> int:
        mem = [None] * (N + 1)
        return self.helper(N, mem)

    def helper(self, N: int, mem: List[int]) -> int:
        if N < 2:
            return N
        if mem[N] is None:
            mem[N] = self.fib(N - 1) + self.fib(N - 2)
        return mem[N]


# Table lookup. Time: O(1). Space: O(n)
class Solution4:
    def fib(self, N: int) -> int:
        return [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
            28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040
        ][N]


# Dynamic programming with lru_cache. Time: O(n). Space: O(n)
class Solution5:
    def fib(self, N: int) -> int:
        return self.helper(N)

    @lru_cache()
    def helper(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    import Test

    Test.test([Solution().fib, Solution2().fib, Solution3().fib, Solution4().fib, Solution5().fib], [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (30, 832040),
    ])

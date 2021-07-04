import math

"""
0 1 2 3 4 5 6 7 8 9 10
*
    *
          *
                  *

9, 22, 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, and 100.
(1 + k) * k / 2 >= n
1/2 * k^2 + 1/2 * k - n >= 0
k^2 + k -2n >= 0
k = -1 + sqrt(4 * 2n) / 2
"""


# Brute Force. Time: O(n). Space: O(1)
class Solution:
    def twoEggDrop(self, n: int) -> int:
        drop = 0
        while n > 0:
            drop += 1
            n -= drop
        return drop


# Formula. Time: O(1). Space: O(1)
class Solution2:
    def twoEggDrop(self, n: int) -> int:
        return int(0.5 * (-1 + math.sqrt(8 * n))) + 1


if __name__ == '__main__':
    import Test

    Test.test([Solution().twoEggDrop, Solution2().twoEggDrop], [
        (2, 2),
        (10, 4),
        (100, 14),
    ])

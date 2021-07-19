from typing import List

"""
[1, 2, 5], 11
Choice Amount Change
5      6      1
5      1      2
1      0      3

[4, 5], 8
Choice Amount Change
5      3      1
4      4      1
4      0      2
"""


# Dynamic Programming.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [0] + [(float('inf'))] * amount
        for i in range(1, amount + 1):
            mem[i] = 1 + min(mem[i - c] if i >= c else float('inf') for c in coins)
        if mem[-1] == float('inf'):
            return -1
        return mem[-1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().coinChange], [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([1], 1), 1),
        (([1], 2), 2),
        (([186, 419, 83, 408], 6249), 20),
    ])

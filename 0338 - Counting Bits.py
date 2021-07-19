from typing import List

"""
0  => 0    0
1  => 1    1
2  => 10   1
3  => 11   2
4  => 100  1
5  => 101  2
6  => 110  2
7  => 111  3
8  => 1000 1
9  => 1001 2
10 => 1010 2
11 => 1011 3
12 => 1100 2 

denominator [0, 1, 2, 4, 4, 8, 8, 8, 8]
result      [0, 1, 1, 2, 1, 2, 2, 3, 1]
"""


# Dynamic Programming. Time: O(n). Space: O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]
        denominator = 1
        for i in range(1, n + 1):
            if i % denominator == 0:
                results.append(1)
                denominator *= 2
            else:
                results.append(1 + results[i % (denominator // 2)])
        return results


if __name__ == '__main__':
    import Test

    Test.test(Solution().countBits, [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ])

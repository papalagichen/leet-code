import math


class Solution:
    lookup = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }

    def numSquares(self, n: int) -> int:
        if n in self.lookup:
            return self.lookup[n]
        least_num = n
        for i in range(int(math.sqrt(n)), 1, -1):
            count = 1 + self.numSquares(n - i * i)
            if count < least_num:
                least_num = count
        self.lookup[n] = least_num
        return least_num


if __name__ == '__main__':
    import Test

    Test.test(Solution().numSquares, [
        (1, 1),
        (3, 3),
        (4, 1),
        (12, 3),
        (13, 2),
        (34, 2),
    ])

class Solution:
    def trailingZeroes(self, n):
        s = 1
        c = 0
        while s <= n:
            s *= 5
            c += n / s
        return c

if __name__ == '__main__':
    import Test

    Test.test(Solution().trailingZeroes, [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 1),
        (10, 2),
        (15, 3),
        (30, 7),
        (1808548329, 452137076),
    ])

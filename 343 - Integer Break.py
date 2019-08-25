class Solution:
    cache = {
        1: 1,
        2: 1,
        3: 2,
        4: 4,
        5: 6,
        6: 9,
    }

    def integerBreak(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        max_product = 1
        for i in range(1, int(n / 2) + 1):
            product = i * self.integerBreak(n - i)
            if product > max_product:
                max_product = product
        self.cache[n] = max_product
        return max_product


if __name__ == '__main__':
    import Test

    Test.test(Solution().integerBreak, [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 6),
        (6, 9),
        (7, 12),
        (8, 18),
        (10, 36),
        (15, 243),
    ])

# Dynamic programming. Time: O(n). Space: O(n)
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


# Calculate only 2 and 3. Time: O(1). Space: O(1)
class Solution2:
    def integerBreak(self, n: int) -> int:
        a = n % 3
        if n > 3:
            result = 3 ** ((n // 3) - (1 if a == 1 else 0))
        elif n < 3:
            return 1
        else:
            return 2
        if a == 1:
            return result * 4
        elif a == 2:
            return result * 2
        else:
            return result


if __name__ == '__main__':
    import Test

    Test.test([Solution().integerBreak, Solution2().integerBreak], [
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

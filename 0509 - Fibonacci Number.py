# Dynamic programming. Time: O(n). Space: O(1)
class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a


# Table lookup. Time: O(1). Space: O(n)
class Solution2:
    def fib(self, N: int) -> int:
        return [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
            28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040
        ][N]


if __name__ == '__main__':
    import Test

    Test.test([Solution().fib, Solution2().fib], [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (30, 832040),
    ])

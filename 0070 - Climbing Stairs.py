# Dynamic programming. Time: O(n). Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    import Test

    Test.test(Solution().climbStairs, [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (35, 14930352),
    ])

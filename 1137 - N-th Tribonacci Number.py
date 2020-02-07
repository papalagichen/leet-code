# Dynamic programming. Time: O(n). Space: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a + b + c
        return a


# Table lookup. Time: O(1). Space: O(n)
class Solution2:
    def tribonacci(self, n: int) -> int:
        return [
            0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012,
            121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080,
            98950096, 181997601, 334745777, 615693474, 1132436852, 2082876103
        ][n]


if __name__ == '__main__':
    import Test

    Test.test([Solution().tribonacci, Solution2().tribonacci], [
        (3, 2),
        (4, 4),
        (25, 1389537),
    ])

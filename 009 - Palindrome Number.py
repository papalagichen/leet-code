class Solution:
    def reverse(self, x):
        negative = x < 0
        x = abs(x)
        y = 0
        while x > 0:
            y *= 10
            y += x % 10
            x /= 10
        if y > 2 ** 31:
            return 0
        return y * -1 if negative else y

if __name__ == '__main__':
    import Test
    Test.test(0, Solution().reverse(0))
    Test.test(321, Solution().reverse(123))
    Test.test(-321, Solution().reverse(-123))
    Test.test(1, Solution().reverse(100))
    Test.test(101, Solution().reverse(101))
    Test.test(0, Solution().reverse(1000000003))

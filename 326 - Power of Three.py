class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPowerOfThree, [
        (1, True),
        (3, True),
        (9, True),
        (27, True),
        (0, False),
        (-2, False),
        (2, False),
    ])

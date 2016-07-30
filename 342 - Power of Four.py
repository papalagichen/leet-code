class Solution(object):
    def isPowerOfFour(self, num):
        i = 1
        while i <= num:
            if i == num:
                return True
            i *= 4
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPowerOfFour, [
        (1, True),
        (4, True),
        (5, False),
        (16, True),
        (32, False),
        (-2147483648, False),
    ])

class Solution(object):
    def isPowerOfTwo(self, n):
        i = 1
        while i <= n:
            if i == n:
                return True
            i *= 2
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPowerOfTwo, [
        (0, False),
        (1, True),
        (2, True),
        (4, True),
        (3, False),
        (-1, False),
    ])

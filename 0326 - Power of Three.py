class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


class Solution2(object):
    def isPowerOfThree(self, n):
        return n > 0 and pow(3, 19) % n == 0


if __name__ == '__main__':
    import Test

    Test.test((Solution().isPowerOfThree, Solution2().isPowerOfThree), [
        (1, True),
        (3, True),
        (9, True),
        (27, True),
        (0, False),
        (-2, False),
        (2, False),
    ])

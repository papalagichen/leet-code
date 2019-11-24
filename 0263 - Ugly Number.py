class Solution(object):
    def isUgly(self, num):
        if num == 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1


if __name__ == '__main__':
    import Test

    Test.test(Solution().isUgly, [
        (0, False),
        (1, True),
        (2, True),
        (3, True),
        (5, True),
        (6, True),
        (8, True),
        (14, False),
    ])

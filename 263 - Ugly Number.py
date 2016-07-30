class Solution(object):
    def isUgly(self, num):
        if num == 1:
            return True
        if num <= 0:
            return False
        while num > 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /=3
            elif num % 5 == 0:
                num /=5
            else:
                return False
        return True

if __name__ == '__main__':
    import Test

    Test.test(Solution().isUgly, [
        (1, True),
        (2, True),
        (3, True),
        (5, True),
        (6, True),
        (8, True),
        (14, False),
    ])

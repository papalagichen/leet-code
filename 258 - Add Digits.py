class Solution(object):
    def addDigits(self, num):
        while num > 9:
            num = num / 10 + num % 10
        return num


if __name__ == '__main__':
    import Test

    Test.test(Solution().addDigits, [
        (1, 1),
        (20, 2),
        (38, 2),
    ])

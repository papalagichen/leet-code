class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num ** 0.5 % 1 == 0


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPerfectSquare, [
        (16, True),
        (14, False),
    ])

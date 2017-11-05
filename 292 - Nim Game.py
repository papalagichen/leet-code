class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & 3 != 0


if __name__ == '__main__':
    import Test

    Test.test(Solution().canWinNim, [
        (1, True),
        (2, True),
        (3, True),
        (4, False),
    ])

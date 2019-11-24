class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for a, b in zip(sorted_s, sorted_t):
            if a != b:
                return b
        return sorted_t[-1]


if __name__ == '__main__':
    import Test

    Test.test(Solution().findTheDifference, [
        (('abcd', 'abcde'), 'e'),
    ])

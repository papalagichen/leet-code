class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        for c in s:
            if d[c] != -1:
                return d[c]
        return -1


if __name__ == '__main__':
    import Test

    Test.test(Solution().firstUniqChar, [
        ('leetcode', 0),
        ('loveleetcode', 2),
        ('aabbcc', -1),
    ])

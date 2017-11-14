class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = dict()
        for c in magazine:
            d[c] = 1 + d.get(c, 0)
        for c in ransomNote:
            if d.get(c, 0) == 0:
                return False
            d[c] = d.get(c) - 1
        return True


if __name__ == '__main__':
    import Test

    Test.test(Solution().canConstruct, [
        (('a', 'b'), False),
        (('aa', 'ab'), False),
        (('aa', 'aab'), True),
    ])

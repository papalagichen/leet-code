class Solution(object):
    def isAnagram(self, s, t):
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return cmp(ls, lt) == 0


if __name__ == '__main__':
    import Test

    Test.test(Solution().isAnagram, [
        (('a', 'a'), True),
        (('anagram', 'nagaram'), True),
        (('rat', 'car'), False),
    ])

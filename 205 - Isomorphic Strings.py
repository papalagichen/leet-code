class Solution:
    def isIsomorphic(self, s, t):
        d = {}
        for c1, c2 in zip(s, t):
            if c1 in d:
                if d[c1] != c2:
                    return False
            elif c2 in d.values():
                return False
            else:
                d[c1] = c2
        return True

if __name__ == '__main__':
    import Test

    Test.test(Solution().isIsomorphic, [
        (('', ''), True),
        (('egg', 'add'), True),
        (('foo', 'bar'), False),
        (('paper', 'title'), True),
        (('ab', 'aa'), False),
    ])

class Solution:
    def isValid(self, s):
        a = []
        m = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in m:
                a.append(c)
            elif not a or c != m[a.pop()]:
                return False
        return not a


if __name__ == '__main__':
    import Test

    Test.test(Solution().isValid, [
        ('()', True),
        ('[]', True),
        ('{}', True),
        ('}{', False),
        ('{', False),
        ('()[]{}', True),
        ('([{()}])', True),
        ('(]', False),
        ('([)]', False),
    ])

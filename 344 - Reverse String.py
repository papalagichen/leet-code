class Solution(object):
    def reverseString(self, s):
        l = list(s)
        l.reverse()
        return ''.join(l)


class Solution2(object):
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    import Test

    Test.test((Solution().reverseString, Solution2().reverseString), [
        ('hello', 'olleh'),
    ])

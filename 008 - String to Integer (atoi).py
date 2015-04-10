MAX = 1 << 31


class Solution:
    def atoi(self, s):
        s = s.strip()
        for i in range(len(s)):
            if s[i] not in map(str, range(10)) + ['+', '-']:
                s = s[:i]
                break
        try:
            i = int(s)
        except ValueError:
            return 0
        if i > MAX - 1:
            return MAX - 1
        elif i < -MAX:
            return -MAX
        else:
            return i


if __name__ == '__main__':
    import Test

    Test.test(Solution().atoi, [
        ('123', 123),
        ('0123', 123),
        ('+123', 123),
        ('-123', -123),
        ('   -0012a42', -12),
        ('  123  ', 123),
        ('', 0),
        ('  123  123', 123),
        ('123123123123123123123123', 2147483647),
        ('-123123123123123123123123', -2147483648),
    ])

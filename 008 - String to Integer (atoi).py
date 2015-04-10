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

    Test.test(123, Solution().atoi('123'))
    Test.test(123, Solution().atoi('0123'))
    Test.test(123, Solution().atoi('+123'))
    Test.test(-123, Solution().atoi('-123'))
    Test.test(-12, Solution().atoi('   -0012a42'))
    Test.test(123, Solution().atoi('  123  '))
    Test.test(0, Solution().atoi(''))
    Test.test(123, Solution().atoi('  123  123'))
    Test.test(2147483647, Solution().atoi('123123123123123123123123'))
    Test.test(-2147483648, Solution().atoi('-123123123123123123123123'))

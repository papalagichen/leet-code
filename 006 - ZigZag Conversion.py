class Solution:
    def convert(self, s, n):
        if n == 1:
            return s
        r = ''
        for i in range(n):
            j, f = i, False
            while j < len(s):
                r += s[j]
                if i == 0 or i == n - 1:
                    j += (n - 1) * 2
                else:
                    j += i * 2 if f else (n - i - 1) * 2
                    f ^= True
        return r


if __name__ == '__main__':
    import Test

    Test.test(Solution().convert, [
        (('PAYPALISHIRING', 2), 'PYAIHRNAPLSIIG'),
        (('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR'),
        (('PAYPALISHIRING', 4), 'PINALSIGYAHRPI'),
        (('PAYPALISHIRING', 5), 'PHASIYIRPLIGAN'),
        (('A', 1), 'A'),
    ])

class Solution:
    def convertToTitle(self, n):
        s = ''
        while n > 0:
            if n % 26 == 0:
                s = 'Z' + s
                n /= 27
            else:
                s = chr(ord('A') - 1 + n % 26) + s
                n /= 26
        return s


if __name__ == '__main__':
    import Test

    Test.test(Solution().convertToTitle, [
        (1, 'A'),
        (2, 'B'),
        (25, 'Y'),
        (26, 'Z'),
        (27, 'AA'),
        (28, 'AB'),
        (51, 'AY'),
        (52, 'AZ'),
        (53, 'BA'),
    ])

class Solution:
    def romanToInt(self, s):
        d = {
            'i': 1,
            'v': 5,
            'x': 10,
            'l': 50,
            'c': 100,
            'd': 500,
            'm': 1000,
        }
        last, a = 0, 0
        for c in s.lower():
            if last < d[c]:
                a -= 2 * last
            a += d[c]
            last = d[c]
        return a


if __name__ == '__main__':
    import Test

    Test.test(Solution().romanToInt, [
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
        ('II', 2),
        ('III', 3),
        ('XI', 11),
        ('XX', 20),
        ('IV', 4),
        ('IX', 9),
        ('IL', 49),
        ('MCMXCVI', 1996),
        ('MCMIV', 1904),
    ])

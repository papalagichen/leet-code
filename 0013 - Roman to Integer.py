D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s):
        last, a = 0, 0
        for c in s:
            if last < D[c]:
                a -= 2 * last
            a += D[c]
            last = D[c]
        return a


class Solution2:
    def romanToInt(self, s):
        a = 0
        for i in reversed(range(len(s))):
            if i == len(s) - 1 or D[s[i]] >= D[s[i + 1]]:
                a += D[s[i]]
            else:
                a -= D[s[i]]
        return a


class Solution3:
    def romanToInt(self, s):
        ans = 0
        current = 0
        for i in range(len(s) - 1, -1, -1):
            if D[s[i]] < current:
                ans -= D[s[i]]
            else:
                ans += D[s[i]]
            current = D[s[i]]
        return ans


if __name__ == '__main__':
    import Test

    Test.test([Solution().romanToInt, Solution2().romanToInt, Solution3().romanToInt], [
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

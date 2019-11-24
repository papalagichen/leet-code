class Solution:
    def titleToNumber(self, s):
        n = 0
        for c in s:
            n = n * 26 + ord(c) - ord('A') + 1
        return n

if __name__ == '__main__':
    import Test

    Test.test(Solution().titleToNumber, [
        ('A', 1),
        ('B', 2),
        ('Z', 26),
        ('AA', 27),
        ('AB', 28),
    ])

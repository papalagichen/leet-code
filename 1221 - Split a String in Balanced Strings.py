class Solution:
    def balancedStringSplit(self, s: str) -> int:
        split = 0
        balance = 0
        for c in s:
            if c == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                split += 1
        return split


if __name__ == '__main__':
    import Test

    Test.test(Solution().balancedStringSplit, [
        ('RLRRLLRLRL', 4),
        ('RLLLLRRRLR', 3),
        ('LLLLRRRR', 1),
    ])

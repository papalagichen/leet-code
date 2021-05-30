class Solution:
    def minSwaps(self, s: str) -> int:
        zero_start = self.check_zero_start(s)
        one_start = self.check_one_start(s)
        if zero_start >= 0 and one_start >= 0:
            return min(zero_start, one_start)
        if zero_start > 0:
            return zero_start
        if one_start > 0:
            return one_start
        if zero_start == 0 or one_start == 0:
            return 0
        return -1

    def check_zero_start(self, s) -> int:
        to_one, to_zero = 0, 0
        for i in range(len(s)):
            c = s[i]
            expected = '0' if i % 2 == 0 else '1'
            if c != expected:
                if c == '0':
                    to_one += 1
                else:
                    to_zero += 1
        if to_one != to_zero:
            return -1
        if to_one == to_zero:
            return to_one

    def check_one_start(self, s) -> int:
        to_one, to_zero = 0, 0
        for i in range(len(s)):
            c = s[i]
            expected = '0' if i % 2 == 1 else '1'
            if c != expected:
                if c == '0':
                    to_one += 1
                else:
                    to_zero += 1
        if to_one != to_zero:
            return -1
        if to_one == to_zero:
            return to_one


if __name__ == '__main__':
    import Test

    Test.test(Solution().minSwaps, [
        ('111000', 1),
        ('010', 0),
        ('1110', -1),
        ('100', 1),
        ('10', 0),
    ])

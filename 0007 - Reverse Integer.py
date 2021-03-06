MAX = 1 << 31


class Solution:
    def reverse(self, x):
        negative = x < 0
        x = abs(x)
        y = 0
        while x > 0:
            y *= 10
            y += x % 10
            x /= 10
        if y > MAX:
            return 0
        return y * -1 if negative else y


class Solution2:
    def reverse(self, x):
        negative = x < 0
        x = int(str(abs(x))[::-1])
        if x > MAX:
            return 0
        return x * -1 if negative else x


if __name__ == '__main__':
    import Test

    Test.test((Solution().reverse, Solution2().reverse), [
        (0, 0),
        (123, 321),
        (-123, -321),
        (100, 1),
        (101, 101),
        (1000000003, 0),
    ])

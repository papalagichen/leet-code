class Solution:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        d = 7
        while d <= n:
            d *= 7
        s = ""
        d //= 7
        while n > 0 or d > 0:
            if n == 0 and d != 1:
                s += "0"
            else:
                s += str(n // d)
                n %= d
            d //= 7
        return s if num >= 0 else "-{}".format(s)


class Solution2:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        n = abs(num)
        s = ""
        while n > 0:
            s += str(n % 7)
            n //= 7
        s = s[::-1]
        return s if num >= 0 else "-{}".format(s)


if __name__ == '__main__':
    import Test

    Test.test([Solution().convertToBase7, Solution2().convertToBase7], [
        (100, "202"),
        (14, "20"),
        (-7, "-10"),
        (0, "0"),
    ])

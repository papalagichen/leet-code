class Solution:
    def isHappy(self, n):
        s = set()
        while n != 1:
            n = self.digits_square_sum(n)
            if n in s:
                return False
            s.add(n)
        return True

    def digits_square_sum(self, num):
        s = 0
        while num:
            s += (num % 10) ** 2
            num /= 10
        return s


if __name__ == '__main__':
    import Test

    Test.test(Solution().isHappy, [
        (1, True),
        (19, True),
    ])

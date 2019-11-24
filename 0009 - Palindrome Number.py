class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        a, b = x, 0
        while a:
            b = b * 10 + a % 10
            a /= 10
        return x == b


if __name__ == '__main__':
    import Test

    Test.test(Solution().isPalindrome, [
        (12321, True),
        (123321, True),
        (123, False),
        (1, True),
        (-1, False),
        (-123, False),
        (-2147447412, False),
    ])

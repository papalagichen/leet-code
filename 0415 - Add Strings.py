import itertools


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1:
            return num2
        elif not num2:
            return num1

        total = ""
        carry = 0

        for a, b in itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            x = int(a) + int(b) + carry
            carry = x / 10
            total += str(x % 10)

        if carry:
            total += str(carry)

        return total[::-1]


if __name__ == '__main__':
    import Test

    Test.test(Solution().addStrings, [
        (("", ""), ""),
        (("", "1"), "1"),
        (("1", "1"), "2"),
        (("0", "0"), "0"),
        (("5", "5"), "10"),
        (("55", "55"), "110"),
        (("55", "5"), "60"),
        (("109", "1"), "110"),
    ])

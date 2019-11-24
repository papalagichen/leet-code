class Solution:
    def addBinary(self, a, b):
        if not a or not b:
            return a or b
        return "{:b}".format(int(a, 2) + int(b, 2))


class Solution2:
    def addBinary(self, a, b):
        if not a or not b:
            return a or b
        return bin(int(a, 2) + int(b, 2)).split('b')[1]


class Solution3:
    def addBinary(self, a, b):
        return self.int_to_binary_string(self.binary_string_to_int(a) + self.binary_string_to_int(b))

    def binary_string_to_int(self, s):
        if not s:
            return 0
        return reduce(lambda x, y: x + y, [int(x) * 2 ** y for x, y in zip(list(s), range(len(s) - 1, -1, -1))])

    def int_to_binary_string(self, n):
        s = ''
        while n:
            s = str(n & 1) + s
            n >>= 1
        return s


class Solution4:
    def addBinary(self, a, b):
        a = ' ' * (len(b) - len(a)) + a
        b = ' ' * (len(a) - len(b)) + b
        s = carry = ''
        for i, j in zip(list(a[::-1]), list(b[::-1])):
            count = (i + j + carry).count('1')
            carry = '' if count < 2 else '1'
            s = ('1' if count % 2 else '0') + s
        return carry + s


if __name__ == '__main__':
    import Test

    Test.test((Solution().addBinary, Solution2().addBinary, Solution3().addBinary, Solution4().addBinary), [
        (('', '1'), '1'),
        (('1', ''), '1'),
        (('1', '1'), '10'),
        (('11', '1'), '100'),
        (('11', '11'), '110'),
        (('10', '10'), '100'),
    ])

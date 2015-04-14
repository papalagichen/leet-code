class Solution:
    def reverseBits(self, n):
        s = "{:b}".format(n)
        return int(('0' * (32 - len(s)) + s)[::-1], 2)


class Solution2:
    def reverseBits(self, n):
        s = self.int_to_binary_string(n)
        return self.binary_string_to_int(('0' * (32 - len(s)) + s)[::-1])

    def binary_string_to_int(self, s):
        return reduce(lambda x, y: x + y, [int(x) * 2 ** y for x, y in zip(list(s), range(len(s) - 1, -1, -1))])

    def int_to_binary_string(self, n):
        s = ''
        while n:
            s = str(n & 1) + s
            n >>= 1
        return s


if __name__ == '__main__':
    import Test

    Test.test((Solution().reverseBits, Solution2().reverseBits), [
        (0, 0),
        (1, 2 ** 31),
        (43261596, 964176192),
    ])

class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            digits[i] = carry % 10
            carry /= 10
        return [carry] + digits if carry else digits


class Solution2:
    def plusOne(self, digits):
        total = 0
        for d in digits:
            total = 10 * total + d
        total += 1
        s = []
        while total:
            s.insert(0, total % 10)
            total /= 10
        return s


if __name__ == '__main__':
    import Test

    Test.test((Solution().plusOne, Solution2().plusOne), [
        ([0], [1]),
        ([9], [1, 0]),
        ([1, 2, 3], [1, 2, 4]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ])

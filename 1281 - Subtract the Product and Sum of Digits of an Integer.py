class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            digit = int(n % 10)
            product *= digit
            total += digit
            n = int(n / 10)
        return product - total


class Solution2:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for c in str(n):
            digit = int(c)
            product *= digit
            total += digit
        return product - total


if __name__ == '__main__':
    import Test

    Test.test([Solution().subtractProductAndSum, Solution2().subtractProductAndSum], [
        (234, 15),
        (4421, 21),
    ])

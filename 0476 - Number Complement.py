class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        complement = 0
        counter = 1
        while num > 0:
            if num & 1 == 0:
                complement += counter
            num >>= 1
            counter <<= 1
        return complement


if __name__ == '__main__':
    import Test

    Test.test(Solution().findComplement, [
        (5, 2),
        (7, 0),
    ])

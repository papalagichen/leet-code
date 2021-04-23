class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        complement = 0
        counter = 1
        while N > 0:
            if N & 1 == 0:
                complement += counter
            N >>= 1
            counter <<= 1
        return complement


if __name__ == '__main__':
    import Test

    Test.test(Solution().bitwiseComplement, [
        (0, 1),
        (1, 0),
        (5, 2),
        (7, 0),
    ])

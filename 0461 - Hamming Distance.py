class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x > 0 or y > 0:
            if x & 1 != y & 1:
                distance += 1
            x >>= 1
            y >>= 1
        return distance


if __name__ == '__main__':
    import Test

    Test.test(Solution().hammingDistance, [
        ((0, 0), 0),
        ((1, 2), 2),
        ((1, 4), 2),
        ((3, 1), 1),
    ])

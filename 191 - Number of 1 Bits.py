class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


class Solution2:
    def hammingWeight(self, n):
        count = 0
        while n:
            count += 1
            n &= (n - 1)
        return count


if __name__ == '__main__':
    import Test

    Test.test((Solution().hammingWeight, Solution2().hammingWeight), [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (11, 3),
        (127, 7),
        (128, 1),
    ])

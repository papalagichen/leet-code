class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num & 1 > 0:
                num -= 1
            else:
                num //= 2
            count += 1
        return count


if __name__ == '__main__':
    import Test

    Test.test(Solution().numberOfSteps, [
        (0, 0),
        (1, 1),
        (2, 2),
        (8, 4),
        (14, 6),
    ])

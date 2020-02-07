import math


# Two pointers. Time: O(sqrt(n)). Space: 1
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i <= j:
            square_sum = i * i + j * j
            if square_sum == c:
                return True
            if square_sum < c:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().judgeSquareSum, [
        (5, True),
        (3, False),
        (2, True),
        (1, True),
        (1000000000, True),
    ])

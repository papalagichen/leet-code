from typing import List


class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 - sum(int(c) for c in str(min(A))) % 2


if __name__ == '__main__':
    import Test

    Test.test(Solution().sumOfDigits, [
        ([34, 23, 1, 24, 75, 33, 54, 8], 0),
        ([99, 77, 33, 66, 55], 1),
    ])

from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        for i in range(len(arr) - 2):
            a, b, c = arr[i:i + 3]
            if b - a == c - b:
                continue
            if abs(b - a) < abs(c - b):
                return b + (b - a)
            else:
                return a + (c - b)
        return arr[0]


if __name__ == '__main__':
    import Test

    Test.test(Solution().missingNumber, [
        ([5, 7, 11, 13], 9),
        ([15, 13, 12], 14),
        ([1, 2, 3, 5], 4),
        ([0, 0, 0, 0], 0),
    ])

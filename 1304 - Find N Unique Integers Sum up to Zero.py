from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, n // 2 + 1):
            result += [i, -i]
        return result if n % 2 == 0 else result + [0]


if __name__ == '__main__':
    import Test

    Test.test(Solution().sumZero, [
        (5, [-2, -1, 0, 1, 2]),
        (3, [-1, 0, 1]),
        (1, [0]),
    ], sort_result=True)

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.helper(1, n + 1, k)

    def helper(self, start: int, end: int, k: int):
        results = []
        if k > 0:
            for i in range(start, end):
                for result in self.helper(i + 1, end, k - 1):
                    results.append([i] + result)
        else:
            results.append([])
        return results


if __name__ == '__main__':
    import Test

    Test.test(Solution().combine, [
        ((0, 0), [
            []
        ]),
        ((4, 1), [
            [1],
            [2],
            [3],
            [4],
        ]),
        ((4, 2), [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
        ]),
        ((4, 3), [
            [1, 2, 3],
            [1, 2, 4],
            [1, 3, 4],
            [2, 3, 4]
        ]),
    ])

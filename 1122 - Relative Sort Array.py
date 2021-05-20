from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for n in arr1:
            d[n] = d.get(n, 0) + 1
        o = []
        for n in arr2:
            o.extend([n] * d.get(n))
            del d[n]
        for n in sorted(d):
            o.extend([n] * d.get(n))
        return o


if __name__ == '__main__':
    import Test

    Test.test(Solution().relativeSortArray, [
        (([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
        (([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]), [22, 28, 8, 6, 17, 44]),
    ])

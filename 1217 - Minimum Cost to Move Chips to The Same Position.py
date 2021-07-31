from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count, even_count = 0, 0
        for n in position:
            if n & 1 == 1:
                odd_count += 1
            else:
                even_count += 1
        return min(odd_count, even_count)


if __name__ == '__main__':
    import Test

    Test.test([Solution().minCostToMoveChips], [
        ([1], 0),
        ([1, 2, 3], 1),
        ([2, 2, 2, 3, 3], 2),
        ([1, 1000000000], 1),
    ])

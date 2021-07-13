from typing import List

"""
[2]
[3, 4] => [5, 6]
[6, 5, 7] => [11, 10, 13]
"""


# Dynamic Programming top down. Time: O(n). Space: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_totals = triangle[0]
        for i in range(1, len(triangle)):
            temp_totals = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                if j == 0:
                    temp_totals[j] = min_totals[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    temp_totals[j] = min_totals[j - 1] + triangle[i][j]
                else:
                    temp_totals[j] = min(min_totals[j - 1] + triangle[i][j], min_totals[j] + triangle[i][j])
            min_totals = temp_totals
        return min(min_totals)


# Dynamic Programming bottom up. Time: O(n). Space: O(1)
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_totals = triangle[-1]
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                min_totals[j] = triangle[i][j] + min(min_totals[j], min_totals[j + 1])
        return min_totals[0]


if __name__ == '__main__':
    import Test

    Test.test([Solution().minimumTotal, Solution2().minimumTotal], [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]], -10),
    ])

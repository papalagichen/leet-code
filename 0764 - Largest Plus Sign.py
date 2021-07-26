from typing import List

"""
[(5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
[(5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
[(5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
[(5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]
[(5, 5), (5, 5), (0, 0), (5, 5), (5, 5)]

After scan

[(1, 1), (1, 2), (1, 3), (1, 2), (1, 1)]
[(2, 1), (2, 2), (2, 3), (2, 2), (2, 1)]
[(3, 1), (3, 2), (2, 3), (3, 2), (3, 1)]
[(2, 1), (2, 2), (1, 3), (2, 2), (2, 1)]
[(1, 1), (1, 1), (0, 0), (1, 1), (1, 1)]
"""


# Dynamic Programming. Time: O(m * n). Space: O(m * n)
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        m = [[(n, n)] * n for _ in range(n)]
        for mine in mines:
            m[mine[0]][mine[1]] = (0, 0)
        for i in range(n):
            mines_distance = 1
            for j in range(n):
                if m[i][j] != (0, 0):
                    m[i][j] = (m[i][j][0], min(m[i][j][1], mines_distance))
                    mines_distance += 1
                else:
                    mines_distance = 1
            mines_distance = 1
            for j in reversed(range(n)):
                if m[i][j] != (0, 0):
                    m[i][j] = (m[i][j][0], min(m[i][j][1], mines_distance))
                    mines_distance += 1
                else:
                    mines_distance = 1
        # Vertical
        max_plus_size = 0
        for i in range(n):
            mines_distance = 1
            for j in range(n):
                if m[j][i] != (0, 0):
                    m[j][i] = (min(m[j][i][0], mines_distance), m[j][i][1])
                    mines_distance += 1
                else:
                    mines_distance = 1
            mines_distance = 1
            for j in reversed(range(n)):
                if m[j][i] != (0, 0):
                    m[j][i] = (min(m[j][i][0], mines_distance), m[j][i][1])
                    mines_distance += 1
                else:
                    mines_distance = 1
                max_plus_size = max(max_plus_size, min(m[j][i][0], m[j][i][1]))
        return max_plus_size


if __name__ == '__main__':
    import Test

    Test.test([Solution().orderOfLargestPlusSign], [
        ((5, [[4, 2]]), 2),
        ((1, [[0, 0]]), 0),
        ((2, [[0, 0], [0, 1], [1, 0]]), 1),
        ((5, [[0, 2], [0, 4], [1, 2], [2, 0], [2, 3], [2, 4], [3, 4], [4, 2], [4, 4]]), 2),
        ((5, [[3, 0], [3, 3]]), 3),
        ((5, [[0, 0], [0, 3], [1, 1], [1, 4], [2, 3], [3, 0], [4, 2]]), 1),
        ((10,
          [[0, 0], [0, 1], [0, 2], [0, 7], [1, 2], [1, 3], [1, 9], [2, 3], [2, 5], [2, 7], [2, 8], [3, 2], [3, 5],
           [3, 7], [4, 2], [4, 3], [4, 5], [4, 7], [5, 1], [5, 4], [5, 8], [5, 9], [7, 2], [7, 5], [7, 7], [7, 8],
           [8, 5], [8, 8], [9, 0], [9, 1], [9, 2], [9, 8]]),
         4),
        ((10,
          [[0, 0], [0, 5], [1, 2], [1, 9], [2, 5], [2, 8], [3, 1], [3, 6], [5, 0], [6, 1], [6, 4], [6, 6], [6, 8],
           [7, 8], [7, 9], [8, 1], [8, 8], [9, 0], [9, 1], [9, 2], [9, 4], [9, 5], [9, 6]]),
         4),
    ])

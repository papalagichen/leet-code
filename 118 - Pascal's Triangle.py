class Solution:
    def generate(self, n):
        if n == 0:
            return []
        triangle = [[1]]
        for i in range(1, n):
            row = [0] + triangle[i - 1] + [0]
            for j in range(len(row) - 1):
                row[j] += row[j + 1]
            triangle.append(row[:-1])
        return triangle


class Solution2:
    def generate(self, n):
        triangle = []
        for i in range(n):
            triangle.append([])
            for j in range(i + 1):
                triangle[i].append(1 if j == 0 or j == i else triangle[i - 1][j - 1] + triangle[i - 1][j])
        return triangle


if __name__ == '__main__':
    import Test

    Test.test((Solution().generate, Solution2().generate), [
        (0, []),
        (1, [[1]
             ]),
        (2, [[1],
             [1, 1]
             ]),
        (3, [[1],
             [1, 1],
             [1, 2, 1],
             ]),
        (5, [[1],
             [1, 1],
             [1, 2, 1],
             [1, 3, 3, 1],
             [1, 4, 6, 4, 1]
             ]),
    ])

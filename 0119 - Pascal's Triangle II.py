class Solution:
    def getRow(self, n):
        row = [1, 0]
        for i in range(n):
            row = [0] + row
            for j in range(len(row) - 1):
                row[j] += row[j + 1]
        return row[:-1]


if __name__ == '__main__':
    import Test

    Test.test(Solution().getRow, [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
    ])

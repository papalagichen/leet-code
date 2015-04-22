class Solution:
    def isValidSudoku(self, board):
        for x in range(9):
            if self.has_duplicate(board[x]) or self.has_duplicate([board[y][x] for y in range(9)]):
                return False
        for row in range(3):
            for col in range(3):
                if self.has_duplicate([board[x][y] for x in range(row * 3, row * 3 + 3) for y in range(col * 3, col * 3 + 3)]):
                    return False
        return True

    def has_duplicate(self, nums):
        nums = filter(lambda x: x != '.', nums)
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    import Test

    Test.test(Solution().isValidSudoku, [
        ([['5', '3', '.', '.', '7', '.', '.', '.', '.'],
          ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
          ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
          ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
          ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
          ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
          ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
          ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
          ['.', '.', '.', '.', '8', '.', '.', '7', '9'], ], True),
        ([['.', '.', '.', '.', '5', '.', '.', '1', '.'],
          ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
          ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
          ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
          ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
          ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
          ['.', '.', '4', '.', '.', '.', '.', '.', '.'], ], False),
    ])

from typing import List
from typing import Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, word, (i, j), 0):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, current: Tuple[int, int], index: int) -> bool:
        if index + 1 == len(word):
            return True
        temp, board[current[0]][current[1]] = board[current[0]][current[1]], '#'
        for add in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current[0] + add[0], current[1] + add[1]
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                continue
            if board[x][y] == word[index + 1] and self.dfs(board, word, (x, y), index + 1):
                return True
        board[current[0]][current[1]] = temp
        return False


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int, index: int) -> bool:
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != word[index]:
            return False
        if index + 1 == len(word):
            return True
        temp, board[i][j] = board[i][j], '#',
        result = self.dfs(board, word, i + 1, j, index + 1) or \
                 self.dfs(board, word, i, j + 1, index + 1) or \
                 self.dfs(board, word, i - 1, j, index + 1) or \
                 self.dfs(board, word, i, j - 1, index + 1)
        board[i][j] = temp
        return result


if __name__ == '__main__':
    import Test

    Test.test([Solution().exist, Solution2().exist], [
        (
            (
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ],
                'ABCCED'
            ),
            True
        ),
        (
            (
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ],
                'SEE'
            ),
            True
        ),
        (
            (
                [
                    ['A', 'B', 'C', 'E'],
                    ['S', 'F', 'C', 'S'],
                    ['A', 'D', 'E', 'E']
                ],
                'ABCB'
            ),
            False
        ),
    ])

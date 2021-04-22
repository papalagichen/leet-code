from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        mem = [1] * len(pairs)
        for i in range(1, len(pairs)):
            mem[i] = self.helper(pairs, i, mem)
        return max(mem)

    def helper(self, pairs, i, mem):
        max_length = 1
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                max_length = max(max_length, mem[j] + 1)
        return max_length


if __name__ == '__main__':
    import Test

    Test.test(Solution().findLongestChain, [
        ([[1, 2]], 1),
        ([[1, 2], [2, 3]], 1),
        ([[1, 2], [2, 3], [3, 4]], 2),
        ([[1, 2], [7, 8], [4, 5]], 3),
        ([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]], 4),
    ])

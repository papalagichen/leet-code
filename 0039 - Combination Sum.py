from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSum_helper(candidates, target)

    def combinationSum_helper(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0 or len(candidates) == 0 or candidates[0] > target:
            return []

        candidate = candidates[0]

        if candidate == target:
            return [[candidate]]

        combinations = []

        for combination in self.combinationSum_helper(candidates, target - candidate):
            combinations.append([candidate] + combination)

        for combination in self.combinationSum_helper(candidates[1:], target):
            combinations.append(combination)

        return combinations


if __name__ == '__main__':
    import Test

    Test.test(Solution().combinationSum, [
        (([1, 2], 2), [
            [1, 1],
            [2],
        ]),
        (([2, 3, 6, 7], 7), [
            [2, 2, 3],
            [7],
        ]),
        (([2, 3, 5], 8), [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5],
        ]),
        (([4, 2, 8], 8), [
            [2, 2, 2, 2],
            [2, 2, 4],
            [4, 4],
            [8],
        ]),
    ])

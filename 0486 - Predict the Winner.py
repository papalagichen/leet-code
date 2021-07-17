from functools import lru_cache
from typing import List

"""
Game theory
DFS: Maximum current step + minimum next step (since opponent will maximum their score)

1 5 2
*       *
A B   A B
1 2   2 5
5     1

2 1   1 5
5     2

1 5 233 7
*         *
A   B   A B
1   5   7 233
233 7   1 5

1   7   7 233
233 5   5 1
"""


# Brute Force. Time: O(2^n). Space: O(2^n)
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.get_max_score(nums, 0, len(nums) - 1)
        return score >= sum(nums) - score

    def get_max_score(self, nums: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return nums[start]
        return max(
            nums[start] + min(
                self.get_max_score(nums, start + 2, end),
                self.get_max_score(nums, start + 1, end - 1),
            ),
            nums[end] + min(
                self.get_max_score(nums, start + 1, end - 1),
                self.get_max_score(nums, start, end - 2),
            )
        )


# Dynamic Programming. Time: O(n). Space: O(2^n)
class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        score = self.get_max_score(0, len(nums) - 1)
        return score >= sum(nums) - score

    @lru_cache()
    def get_max_score(self, start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return self.nums[start]
        return max(
            self.nums[start] + min(
                self.get_max_score(start + 2, end),
                self.get_max_score(start + 1, end - 1),
            ),
            self.nums[end] + min(
                self.get_max_score(start + 1, end - 1),
                self.get_max_score(start, end - 2),
            )
        )


class Solution3:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) % 2 == 0:
            return True
        self.nums = nums
        score = self.get_max_score(0, len(nums) - 1)
        return score >= sum(nums) - score

    @lru_cache()
    def get_max_score(self, start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return self.nums[start]
        return max(
            self.nums[start] + min(
                self.get_max_score(start + 2, end),
                self.get_max_score(start + 1, end - 1),
            ),
            self.nums[end] + min(
                self.get_max_score(start + 1, end - 1),
                self.get_max_score(start, end - 2),
            )
        )


if __name__ == '__main__':
    import Test

    Test.test([Solution().PredictTheWinner, Solution2().PredictTheWinner, Solution3().PredictTheWinner], [
        ([1], True),
        ([1, 2], True),
        ([1, 1], True),
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
    ])

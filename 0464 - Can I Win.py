from typing import List, Dict

"""
Game theory
DFS: Maximum current step + minimum next step (since opponent will maximize their score)
If the opponent cannot win in a branch, we are forced to win.

(1..3) 3 => (a) I win

(1 2) 3 => (b) I lose

1 -> 2 => I lose
2 -> 1 => I lose

(1..3) 5 => (c)

1 -> 2 -> 3 => I win *
     3 -> 2 => I win *
2 -> 1 -> 3 => I win
     3      => I lose
3 -> 1 -> 2 => I win
     2      => I lose

(1..3) 6 => (c)

1 -> 2 -> 3 => I win *
     3 -> 2 => I win *

(1..4) 7 => (c)

1 -> 2 -> 3 -> 4 => I lose
2 -> 1 -> 4      => I win *
     3 -> 4      => I win *
     4 -> 1      => I win *
3 -> 1 -> 4      => I win
     2 -> 4      => I win
     4           => I lose
4 -> 1 -> 2      => I win
     2 -> 1      => I win
     3           => I lose
"""


# Dynamic Programming. Time: O(2^n). Space: O(2^n)
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        return self.helper(list(range(1, maxChoosableInteger + 1)), desiredTotal, dict())

    def helper(self, nums: List[int], desiredTotal: int, mem: Dict[tuple, bool]) -> bool:
        key = tuple(nums)
        if key in mem:
            return mem[key]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i], mem):
                mem[key] = True
                return True
        mem[key] = False
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().canIWin, [
        ((10, 11), False),
        ((10, 0), True),
        ((10, 1), True),
        ((10, 40), False),
        ((4, 6), True),
    ])

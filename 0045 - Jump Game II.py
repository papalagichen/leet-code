from typing import List


# Brute force. Time: O(n^2), Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = [0] * len(nums)
        for i in range(len(nums)):
            jump = mem[i]
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if mem[j] == 0:
                    mem[j] = jump + 1
        return mem[-1]


"""
             2 3 1 1 4
current_jump 0 2 2 4 4
max_jump     2 4 4 4 4
jump_count   1 1 2 2 2
"""


# Dynamic Programming: Time: O(n), Space: O(1)
class Solution2:
    def jump(self, nums: List[int]) -> int:
        current_jump = max_jump = jump_count = i = 0
        while current_jump < len(nums) - 1:
            max_jump = max(max_jump, i + nums[i])
            if current_jump == i:
                current_jump = max_jump
                jump_count += 1
            i += 1
        return jump_count


if __name__ == '__main__':
    import Test

    Test.test([Solution().jump, Solution2().jump], [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 2, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([1], 0),
        ([1, 2], 1),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
        ([3, 4, 3, 1, 0, 7, 0, 3, 0, 2, 0, 3], 3)
    ])

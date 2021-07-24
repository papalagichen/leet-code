from typing import List

"""
4 3 2 6
4 + 3 + 2 + 6 = 15
0*4 + 1*3 + 2*2 + 3*6 = 25
0*6 + 1*4 + 2*3 + 3*2 = 25 + 15 - 18 - 6 = 16
0*2 + 1*6 + 2*4 + 3*3 = 16 + 15 - 6 - 2 = 23
0*3 + 1*2 + 2*6 + 3*4 = 23 + 15 - 9 - 3 = 26 max!!
"""


# Brute Force. Time: O(n^2). Space: O(1)
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        max_sum = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, i + len(nums)):
                s += (j - i) * nums[j % len(nums)]
            max_sum = max(max_sum, s)
        return max_sum


# Dynamic Programming. Time: O(n). Space: O(1)
class Solution2:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s, total_sum = 0, 0
        for i in range(len(nums)):
            total_sum += nums[i]
            s += i * nums[i]
        max_rotation_sum = float('-inf')
        for i in reversed(range(len(nums))):
            s += total_sum - nums[i] * len(nums)
            max_rotation_sum = max(max_rotation_sum, s)
        return max_rotation_sum


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxRotateFunction, Solution2().maxRotateFunction], [
        ([4, 3, 2, 6], 26),
        ([3, 2, 6, 4], 26),
        ([100], 0),
    ])

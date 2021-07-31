from typing import List

"""
3 5 2 3
max(3+3, 5+2) = 7

2 3 3 5

2 3 4 4 5 6
"""


# Two Pointers. Time: O(n lg n). Space: (1)
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[i] + nums[-i - 1] for i in range(len(nums) // 2))


if __name__ == '__main__':
    import Test

    Test.test(Solution().minPairSum, [
        ([3, 5, 2, 3], 7),
        ([3, 5, 4, 2, 4, 6], 8),
    ])

from typing import List

"""
-1 2 -3 4

(a) top 3: 4 2 -1
(b) low 3: -3 -1 2

All combination = 
  a1, a2, a3
  a1, a2, b1
  b1, b2, b3
  b1, b2, a1  
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[-1] * nums[-2] * nums[0],
            nums[0] * nums[1] * nums[-1],
            nums[0] * nums[1] * nums[2],
        )


if __name__ == '__main__':
    import Test

    Test.test([Solution().maximumProduct], [
        ([1, 2, 3], 6),
        ([1, 2, 3, 4], 24),
        ([-1, -2, -3], -6),
        ([-1, 2, -3, 4], 12),
    ])

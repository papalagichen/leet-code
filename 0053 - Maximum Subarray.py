from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        total = 0
        for n in nums:
            total = max(n, total + n)
            best = max(best, total)
        return best


if __name__ == '__main__':
    import Test

    Test.test(Solution().maxSubArray, [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    ])

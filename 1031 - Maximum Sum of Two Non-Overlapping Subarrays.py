from typing import List

"""
0, 6, 5, 2, 2, 5, 1, 9, 4
-------  ----
-------     ----
-------        ----
----  -------
"""


# Brute force. Time: O(n^2). Space: O(n)
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sums = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]
        ans = 0
        for i in range(len(nums) - firstLen - secondLen + 1):
            for j in range(i + firstLen, len(nums) - secondLen + 1):
                ans = max(ans, sums[i + firstLen - 1] - (sums[i - 1] if i > 0 else 0)
                          + sums[j + secondLen - 1] - (sums[j - 1] if j > 0 else 0))
        for i in range(len(nums) - firstLen - secondLen + 1):
            for j in range(i + secondLen, len(nums) - firstLen + 1):
                ans = max(ans, sums[i + secondLen - 1] - (sums[i - 1] if i > 0 else 0)
                          + sums[j + firstLen - 1] - (sums[j - 1] if j > 0 else 0))
        return ans


# Dynamic programming. Time: O(n). Space: O(1)
class Solution2:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        max_sum = nums[firstLen + secondLen - 1]
        max1 = nums[firstLen - 1]
        max2 = nums[secondLen - 1]

        for i in range(firstLen + secondLen, len(nums)):
            max1 = max(max1, nums[i - secondLen] - nums[i - firstLen - secondLen])
            max_sum = max(max_sum, max1 + nums[i] - nums[i - secondLen])

        for i in range(firstLen + secondLen, len(nums)):
            max2 = max(max2, nums[i - firstLen] - nums[i - firstLen - secondLen])
            max_sum = max(max_sum, max2 + nums[i] - nums[i - firstLen])

        return max_sum


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxSumTwoNoOverlap, Solution2().maxSumTwoNoOverlap], [
        (([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2), 20),
        (([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2), 29),
        (([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3), 31),
        (([1, 2], 1, 1), 3),
        (([4, 5, 14, 16, 16, 20, 7, 13, 8], 3, 5), 99),
        (([4, 5, 14, 16, 16, 20, 7, 13], 3, 5), 95),
    ])

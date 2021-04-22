from typing import List


# Brute force. Time: 2^n, space: 1 (Time limit exceeded)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.helper(nums, total / 2)

    def helper(self, nums, target) -> bool:
        if target == 0:
            return True
        if target < 0 or len(nums) == 0:
            return False
        return self.helper(nums[1:], target) or self.helper(nums[1:], target - nums[0])


# Dynamic programming. Time: n^2, space: n
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = int(total / 2)
        dp = [False] * (half + 1)  # True denotes the target value can be fulfilled by sum of elements
        dp[0] = True  # target 0 must be fulfilled
        for n in nums:
            for i in range(half, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[half]


if __name__ == '__main__':
    import Test

    Test.test([Solution().canPartition, Solution2().canPartition], [
        ([1], False),
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
          99, 97], False),
    ])

import bisect
from typing import List


# Brute force. Time O(n^3)
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        num_sum = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                rest = target - nums[i] - nums[j]
                for k in range(j + 1, len(nums)):
                    if nums[k] < rest:
                        num_sum += 1
        return num_sum


# Dynamic programming. Time O(n^2)
class Solution2:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        mem = {}
        num_sum = 0
        for i in range(len(nums) - 2):
            if i == 0:
                for j in range(i + 1, len(nums) - 1):
                    for k in range(j + 1, len(nums)):
                        mem[(j, k)] = nums[j] + nums[k]
                        if nums[i] + nums[j] + nums[k] < target:
                            num_sum += 1
            else:
                for pair, sum_of_pair in mem.items():
                    if pair[0] > i and nums[i] + sum_of_pair < target:
                        num_sum += 1
        return num_sum


# Binary search. Time: O(n^2 lg n)
class Solution3:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        num_sum = 0
        for i in range(len(nums) - 2):
            num_sum += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return num_sum

    def twoSumSmaller(self, nums: List[int], start: int, target: int) -> int:
        num_sum = 0
        for i in range(start, len(nums) - 1):
            index = bisect.bisect_left(nums, target - nums[i], lo=i + 1)
            num_sum += index - i - 1
        return num_sum


# Two pointers. Time: O(n^2)
class Solution4:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        num_sum = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    num_sum += right - left
                    left += 1
                else:
                    right -= 1
        return num_sum


if __name__ == '__main__':
    import Test

    Test.test([
        Solution().threeSumSmaller,
        Solution2().threeSumSmaller,
        Solution3().threeSumSmaller,
        Solution4().threeSumSmaller,
    ], [
        (([-2, 0, 1, 3], 2), 2),
        (([-2, 0, 1, 3], 3), 3),
        (([1, 1, -2], 0), 0),
    ])

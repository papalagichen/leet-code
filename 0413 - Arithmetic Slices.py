from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        p = 0
        s = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != nums[i - 1] - nums[i - 2]:
                s += self.helper(i - p)
                p = i - 1
        return s + self.helper(len(nums) - p)

    def helper(self, n):
        if n < 3:
            return 0
        s = 0
        for i in range(3, n + 1):
            s += n - (i - 1)
        return s


class Solution2:
    def __init__(self):
        self.lookup = [0, 0, 0, 1]

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        p = 0
        total = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != nums[i - 1] - nums[i - 2]:
                total += self.helper(i - p)
                p = i - 1
        return total + self.helper(len(nums) - p)

    def helper(self, n):
        if n >= len(self.lookup):
            for i in range(n - len(self.lookup) + 1):
                self.lookup.append(self.lookup[-1] + (self.lookup[-1] - self.lookup[-2]) + 1)
        return self.lookup[n]


if __name__ == '__main__':
    import Test

    Test.test([Solution().numberOfArithmeticSlices, Solution2().numberOfArithmeticSlices], [
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 3, 4], 3),
        ([1], 0),
        ([1, 2, 3, 8, 9, 10], 2),
        ([1, 2, 3, 5, 7, 9], 4),
    ])

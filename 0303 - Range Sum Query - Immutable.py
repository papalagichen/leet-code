from typing import List


# Brute force. Time: O(n). Space: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[x] for x in range(i, j + 1))


# Memoization
class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = [0] * len(nums)
        for i in range(len(nums)):
            self.nums[i] = nums[i] + self.nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - (self.nums[i - 1] if i > 0 else 0)


if __name__ == '__main__':
    import Test

    Test.test([NumArray([-2, 0, 3, -5, 2, -1]).sumRange, NumArray2([-2, 0, 3, -5, 2, -1]).sumRange], [
        ((0, 2), 1),
        ((2, 5), -1),
        ((0, 5), -3),
        ((0, 0), -2),
    ])

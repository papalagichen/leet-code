from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


# https://discuss.leetcode.com/topic/22821/an-general-way-to-handle-all-this-sort-of-questions/2
class Solution2:
    def singleNumber(self, nums):
        a, b = 0, 0
        for i in range(len(nums)):
            a = (a ^ nums[i]) & ~b
            b = (b ^ nums[i]) & ~a
        return a


if __name__ == '__main__':
    import Test

    Test.test((Solution().singleNumber, Solution2().singleNumber), [
        ([1, 1, 1, 2, 2, 2, 3, 5, 3, 3, 4, 4, 4], 5),
    ])

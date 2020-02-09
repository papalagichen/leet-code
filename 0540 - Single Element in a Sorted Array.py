from typing import List


# Brute force. Time: O(n). Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


# Binary search. Time: O(lg n). Space: O(1)
class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (right + left) // 2
            result = self.check_left_right(nums, middle)
            if result == 0:
                return nums[middle]
            elif result == -1:
                left = middle + 1
            else:
                right = middle - 1
        return nums[left]

    # return -1 if left
    # return 0 if found
    # return 1 if right
    def check_left_right(self, nums: List[int], index: int) -> int:
        if index == len(nums) - 1:
            return 0 if nums[index] != nums[index - 1] else 1
        if nums[index - 1] != nums[index] != nums[index + 1]:
            return 0
        if index % 2 == 0:
            return -1 if nums[index] == nums[index + 1] else 1
        else:
            return 1 if nums[index] == nums[index + 1] else -1


if __name__ == '__main__':
    import Test

    Test.test([Solution().singleNonDuplicate, Solution2().singleNonDuplicate], [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([3, 3, 7, 7, 11, 11, 13], 13),
        ([3, 3, 7, 7, 10, 11, 11], 10),
    ])

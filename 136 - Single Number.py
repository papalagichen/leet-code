class Solution:
    def singleNumber(self, nums):
        nums.sort()
        for i in xrange(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


if __name__ == '__main__':
    import Test
    import random

    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
    random.shuffle(nums)

    nums2 = [1, 1, 2, 2, 3, 4, 4, 5, 5]
    random.shuffle(nums2)

    nums3 = [1, 0, 1]
    random.shuffle(nums3)

    Test.test(Solution().singleNumber, [
        (nums, 6),
        (nums2, 3),
        (nums3, 0),
    ])

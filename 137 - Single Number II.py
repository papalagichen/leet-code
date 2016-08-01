class Solution:
    def singleNumber(self, nums):
        nums.sort()
        for i in xrange(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


if __name__ == '__main__':
    import Test

    Test.test(Solution().singleNumber, [
        ([1, 1, 1, 2, 2, 2, 3, 5, 3, 3, 4, 4, 4], 5),
    ])

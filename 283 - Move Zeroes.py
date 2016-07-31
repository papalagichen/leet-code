class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0] * (len(nums) - j)


if __name__ == '__main__':
    import Test

    nums = [0]
    Solution().moveZeroes(nums)
    Test.equal([0], nums)

    nums = [0, 0]
    Solution().moveZeroes(nums)
    Test.equal([0, 0], nums)

    nums = [1]
    Solution().moveZeroes(nums)
    Test.equal([1], nums)

    nums = [1, 2, 3]
    Solution().moveZeroes(nums)
    Test.equal([1, 2, 3], nums)

    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    Test.equal([1, 3, 12, 0, 0], nums)
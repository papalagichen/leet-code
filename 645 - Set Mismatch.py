class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        total = nums[-1]
        duplicate = 0
        for i in xrange(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
            total += nums[i]
        return [duplicate, (1 + len(nums)) * len(nums) / 2 - total + duplicate]


if __name__ == '__main__':
    import Test

    Test.test(Solution().findErrorNums, [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([2, 2], [2, 1]),
        ([1, 2, 2], [2, 3]),
        ([2, 2, 3], [2, 1]),
        ([1, 1, 3], [1, 2]),
    ])

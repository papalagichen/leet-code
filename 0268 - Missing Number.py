class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (1 + len(nums)) * len(nums) / 2 - sum(nums)


if __name__ == '__main__':
    import Test

    Test.test(Solution().missingNumber, [
        ([0, 1, 3], 2),
    ])

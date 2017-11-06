class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        total = (1 + length) * length / 2
        for n in nums:
            total -= n
        return total


if __name__ == '__main__':
    import Test

    Test.test(Solution().missingNumber, [
        ([0, 1, 3], 2),
    ])

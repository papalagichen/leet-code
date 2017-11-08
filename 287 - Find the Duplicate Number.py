class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        # find the circle entry
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        fast = 0
        # find the duplicate
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


if __name__ == '__main__':
    import Test

    Test.test(Solution().findDuplicate, [
        ([1, 2, 3, 4, 4, 4], 4),
        ([1, 2, 3, 3, 3, 3, 4, 5], 3),
        ([1, 1, 2], 1),
        ([1, 1], 1),
        ([1, 3, 4, 2, 2], 2),
    ])

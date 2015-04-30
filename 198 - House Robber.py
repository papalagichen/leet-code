class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) < 3:
            return max(nums[:len(nums)])
        else:
            c1, c2, c3 = nums[0], nums[1], nums[0] + nums[2]
            for n in range(3, len(nums)):
                c1, c2, c3 = c2, c3, nums[n] + max(c1, c2)
            return max(c1, c2, c3)


if __name__ == '__main__':
    import Test

    Test.test(Solution().rob, [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 1, 2, 1, 2], 6),
        ([3, 3, 2, 1], 5),
        ([1, 20, 3, 4, 15, 6], 35),
        ([2, 1, 1, 2], 4),
    ])

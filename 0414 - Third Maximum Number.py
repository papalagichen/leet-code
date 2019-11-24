class Solution(object):
    def thirdMax(self, nums):
        maxs = [float('-inf'), float('-inf'), float('-inf')]
        for n in nums:
            if n not in maxs:
                if n > maxs[0]:
                    maxs = [n, maxs[0], maxs[1]]
                elif n > maxs[1]:
                    maxs = [maxs[0], n, maxs[1]]
                elif n > maxs[2]:
                    maxs = [maxs[0], maxs[1], n]
        return maxs[0] if float('-inf') == maxs[2] else maxs[2]


class Solution2(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


if __name__ == '__main__':
    import Test

    Test.test(Solution().thirdMax, [
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([2, 2, 2, 2], 2),
        ([2, 2, 2, 1], 2),
        ([5, 2, 2], 5),
        ([1, 2, 2], 2),
    ])
    Test.test(Solution2().thirdMax, [
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([2, 2, 2, 2], 2),
        ([2, 2, 2, 1], 2),
        ([5, 2, 2], 5),
        ([1, 2, 2], 2),
    ])

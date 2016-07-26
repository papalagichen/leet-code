class Solution(object):
    def fourSum(self, nums, target):
        quads = []

        if len(nums) < 4:
            return quads

        nums.sort()

        for i in xrange(0, len(nums) - 3):
            for j in xrange(i + 1, len(nums) - 2):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    s = nums[i] + nums[j] + nums[start] + nums[end]
                    if s < target:
                        start += 1
                    elif s > target:
                        end -= 1
                    else:
                        q = [nums[i], nums[j], nums[start], nums[end]]
                        if q not in quads:
                            quads.append(q)
                        start += 1
                        end -= 1
        return quads


if __name__ == '__main__':
    import Test

    Test.test(Solution().fourSum, [
        (([1, 0, -1, 0, -2, 2], 0), [
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1]
        ]),
        (([1, 1, 1, 1], 4), [
            [1, 1, 1, 1]
        ]),
    ])

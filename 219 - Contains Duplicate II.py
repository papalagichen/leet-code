class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in xrange(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False


if __name__ == '__main__':
    import Test

    Test.test(Solution().containsNearbyDuplicate, [
        (([1, 2, 3, 4, 1], 3), False),
        (([1, 2, 3, 4, 1], 4), True),
        (([1, 2, 3, 4, 5], 10), False),
        (([1, 0, 1, 1], 1), True),
    ])

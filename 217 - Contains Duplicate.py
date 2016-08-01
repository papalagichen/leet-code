class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in xrange(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


class Solution2(object):
    def containsDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                return True
            d[n] = n
        return False


if __name__ == '__main__':
    import Test

    Test.test((Solution().containsDuplicate, Solution2().containsDuplicate), [
        ([0], False),
        ([1], False),
        ([1, 1], True),
        ([1, 0], False),
        ([1, 0, 1], True),
    ])

class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        nums.sort()
        n, last = nums[0], 0
        for n in nums:
            if n <= 0:
                continue
            if n - last > 1:
                return last + 1
            last = n
        return n + 1


class Solution2(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                a, b = i, nums[i] - 1
                nums[a], nums[b] = nums[b], nums[a]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    import Test

    Test.test((Solution().firstMissingPositive, Solution2().firstMissingPositive), [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
    ])

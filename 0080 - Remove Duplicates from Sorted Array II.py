class Solution(object):
    def removeDuplicates(self, nums):
        count, last, i = 0, None, 0
        while i < len(nums):
            if last == nums[i]:
                if count == 2:
                    nums.pop(i)
                    continue
                count += 1
            else:
                last = nums[i]
                count = 1
            i += 1


class Solution2(object):
    def removeDuplicates(self, nums):
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 2] and nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1


class Solution3(object):
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1


if __name__ == '__main__':
    import Test

    nums = [1, 1, 1, 2, 2, 3]
    Solution().removeDuplicates(nums)
    Test.equal([1, 1, 2, 2, 3], nums)

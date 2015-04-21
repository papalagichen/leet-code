class Solution:
    def rotate(self, nums, k):
        i, saver = 0, None
        for x in range(len(nums)):
            if saver is None:
                saver = nums[i]
                nums[i] = None
            saver, nums[(i + k) % len(nums)] = nums[(i + k) % len(nums)], saver
            i = i + 1 if saver is None else (i + k) % len(nums)


if __name__ == '__main__':
    import Test

    a = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(a, 0)
    Test.equal([1, 2, 3, 4, 5, 6, 7], a)

    a = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(a, 3)
    Test.equal([5, 6, 7, 1, 2, 3, 4], a)

    a = [1, 2, 3, 4, 5, 6]
    Solution().rotate(a, 11)
    Test.equal([2, 3, 4, 5, 6, 1], a)

    a = [1, 2, 3, 4, 5, 6]
    Solution().rotate(a, 2)
    Test.equal([5, 6, 1, 2, 3, 4], a)

    a = [1, 2, 3]
    Solution().rotate(a, 3)
    Test.equal([1, 2, 3], a)

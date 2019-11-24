class Solution:
    def largestNumber(self, nums):
        if all([n == 0 for n in nums]):
            return '0'
        nums = map(str, nums)
        nums = sorted(nums, cmp=lambda x, y: cmp(x + y, y + x), reverse=True)
        return ''.join(nums)


if __name__ == '__main__':
    import Test

    Test.test(Solution().largestNumber, [
        ([3, 30, 34, 5, 9], '9534330'),
        ([3, 30], '330'),
        ([3, 39], '393'),
        ([0, 0], '0'),
        ([121, 12], '12121'),
        ([830, 8308], '8308 830', '8308 308'),
    ])

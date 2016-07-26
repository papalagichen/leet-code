class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        return nums[n / 2] if n % 2 == 1 else (nums[n / 2 - 1] + nums[n / 2]) / 2.0


if __name__ == '__main__':
    import Test

    Test.test(Solution().findMedianSortedArrays, [
        (([1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 8, 9]), 6),
        (([], [2, 3]), 2.5),
    ])

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        intersection = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1

        return intersection


if __name__ == '__main__':
    import Test

    Test.test(Solution().intersect, [
        (([], []), []),
        (([1, 2, 2, 1], [2, 2]), [2, 2]),
    ])

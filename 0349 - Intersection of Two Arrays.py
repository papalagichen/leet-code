class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))


class Solution2(object):
    def intersection(self, nums1, nums2):
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
                if len(intersection) == 0 or nums1[i] != intersection[-1]:
                    intersection.append(nums1[i])
                i += 1
                j += 1

        return intersection


if __name__ == '__main__':
    import Test

    Test.test((Solution().intersection, Solution2().intersection), [
        (([1, 2, 2, 1], [2, 2]), [2]),
    ])

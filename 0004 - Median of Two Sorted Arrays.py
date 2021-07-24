# Invoke sort function. Time: O(log n). Space: O(n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        return nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[n // 2]) / 2


# Combine sorted arrays. Time: O(n). Space: O(n)
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        all = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                all.append(nums1[i])
                i += 1
            else:
                all.append(nums2[j])
                j += 1
        if i == len(nums1):
            all.extend(nums2[j:])
        else:
            all.extend(nums1[i:])
        return all[len(all) // 2] if len(all) % 2 == 1 else (all[len(all) // 2 - 1] + all[len(all) // 2]) / 2


if __name__ == '__main__':
    import Test

    Test.test(Solution2().findMedianSortedArrays, [
        (([1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 8, 9]), 6),
        (([], [2, 3]), 2.5),
    ])

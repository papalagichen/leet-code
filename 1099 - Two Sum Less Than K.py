import bisect
from typing import List


# Brute force. Time: O(n^2)
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        a = sorted([x for x in A if x < K])
        max_sum = -1
        for i in range(len(a)):
            for j in range(len(a) - 1, i, -1):
                if a[i] + a[j] < K:
                    max_sum = max(max_sum, a[i] + a[j])
        return max_sum


# Binary search. Time: O(n lg n)
class Solution2:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_sum = -1
        for i in range(len(A) - 1):
            index = bisect.bisect_left(A, K - A[i], lo=i + 1, hi=len(A) - 1)
            if A[index] + A[i] < K:
                max_sum = max(max_sum, A[index] + A[i])
            elif index - 1 != i and A[index - 1] + A[i] < K:
                max_sum = max(max_sum, A[index - 1] + A[i])
        return max_sum


# Two pointers. Time: O(n^2)
class Solution3:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_sum = -1
        for i in range(len(A) - 1):
            left = i
            right = len(A) - 1
            while left < right:
                if A[left] + A[right] < K:
                    max_sum = max(max_sum, A[left] + A[right])
                    left += 1
                else:
                    right -= 1
        return max_sum


if __name__ == '__main__':
    import Test

    Test.test([Solution().twoSumLessThanK, Solution2().twoSumLessThanK, Solution3().twoSumLessThanK], [
        (([34, 23, 1, 24, 75, 33, 54, 8], 60), 58),
        (([10, 20, 30], 15), -1),
        (([173, 891, 643, 806, 77, 547, 600, 808, 591, 302, 344, 670, 650, 307, 835, 241, 599, 773, 956, 62, 196,
           691, 123, 60, 362, 246, 475, 473, 279, 389, 133, 878, 837, 164, 212, 398, 841, 264, 471, 179, 5, 197, 819,
           449, 614, 352, 190, 713, 638, 286],
          1400),
         1399),
        (([973, 478, 246, 883, 265, 900, 21, 130, 143, 235, 846, 198, 17, 964, 685, 584, 796, 329, 579, 373, 500, 944,
           812, 526, 61, 318, 615, 249, 427, 449, 409, 861, 299, 429, 434, 842, 584, 33, 974, 751, 615, 463, 197, 26,
           163, 143, 251, 908, 889, 252],
          900),
         899),
        (([358, 898, 450, 732, 672, 672, 256, 542, 320, 573, 423, 543, 591, 280, 399, 923, 920, 254, 135, 952, 115, 536,
           143, 896, 411, 722, 815, 635, 353, 486, 127, 146, 974, 495, 229, 21, 733, 918, 314, 670, 671, 537, 533, 716,
           140, 599, 758, 777, 185, 549],
          1800),
         1794),
        (([499, 451, 631, 986, 937, 847, 540, 697, 502, 12, 166, 633, 536, 603, 316, 645, 182, 976, 79, 404, 893, 749,
           823, 753, 428, 943, 868, 755, 223, 904, 205, 541, 407, 308, 829, 751, 703, 156, 529, 67, 785, 422, 691, 905,
           928, 706, 594, 203, 548, 662],
          1900),
         1891),
    ])

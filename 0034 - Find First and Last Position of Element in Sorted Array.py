import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect.bisect_left(nums, target)
        last = bisect.bisect_right(nums, target) - 1
        return [
            first if 0 <= first < len(nums) and nums[first] == target else -1,
            last if 0 <= last < len(nums) and nums[last] == target else -1,
        ]


if __name__ == '__main__':
    import Test

    Test.test(Solution().searchRange, [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
        (([], 0), [-1, -1]),
        (([2, 2], 3), [-1, -1]),
    ])

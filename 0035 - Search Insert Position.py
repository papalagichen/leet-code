import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


if __name__ == '__main__':
    import Test

    Test.test(Solution().searchInsert, [
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
    ])

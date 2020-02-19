from typing import List


# Sliding window. Time: O(n). Space: O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start, total, min_length = 0, 0, 0
        for i, n in enumerate(nums):
            total += n
            while total >= s:
                min_length = min(min_length, i - start + 1) if min_length > 0 else i - start + 1
                total -= nums[start]
                start += 1
        return min_length


if __name__ == '__main__':
    import Test

    Test.test(Solution().minSubArrayLen, [
        ((7, [2, 3, 1, 2, 4, 3]), 2),
        ((3, [2, 3, 1, 2, 4, 3]), 1),
        ((1, []), 0),
    ])

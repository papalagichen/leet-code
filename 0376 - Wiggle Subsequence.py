from typing import List


# Dynamic programming. Time: O(n^2). Space: O(n)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_length = 1
        increasing_list = [(nums[0], 1)]
        decreasing_list = [(nums[0], 1)]
        for n in nums[1:]:
            increasing_length = [x[1] for x in increasing_list if x[0] > n]
            if increasing_length:
                max_increasing = max(increasing_length)
                decreasing_list.append((n, max_increasing + 1))
                max_length = max(max_length, max_increasing + 1)
            decreasing_lengths = [x[1] for x in decreasing_list if x[0] < n]
            if decreasing_lengths:
                max_decreasing = max(decreasing_lengths)
                increasing_list.append((n, max_decreasing + 1))
                max_length = max(max_length, max_decreasing + 1)
        return max_length


# Dynamic programming. Time: O(n). Space: O(1)
class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        last_increasing = (nums[0], 1)
        last_decreasing = (nums[0], 1)
        for n in nums[1:]:
            decreasing, increasing = None, None
            if n < last_increasing[0]:
                decreasing = (n, last_increasing[1] + 1)
            if n > last_decreasing[0]:
                increasing = (n, last_decreasing[1] + 1)
            if decreasing:
                last_decreasing = decreasing
            if increasing:
                last_increasing = increasing
        return max(last_increasing[1], last_decreasing[1])


if __name__ == '__main__':
    import Test

    Test.test([Solution().wiggleMaxLength, Solution2().wiggleMaxLength], [
        ([1, 7, 4, 9, 2, 5], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
        ([2, 1, 3], 3),
        ([1], 1),
        ([1, 1, 1], 1),
        ([], 0),
    ])

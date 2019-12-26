from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        length = [0] * len(nums)

        for i in range(len(nums)):
            length[i] = self.look_back(nums[i], nums[:i + 1], length) + 1

        return max(length)

    def look_back(self, target: int, nums: List[int], length: List[int]) -> int:
        max_length = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < target:
                max_length = max(max_length, length[i])

        return max_length


if __name__ == '__main__':
    import Test

    Test.test(Solution().lengthOfLIS, [
        (([1, 2, 3]), 3),
        (([1, 1, 1]), 1),
        (([10, 9, 2, 5, 3, 7, 101, 18]), 4),
        (([-2, -1]), 2),
        (([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6),
    ])

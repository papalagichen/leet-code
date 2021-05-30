from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        previous = nums[0]
        for current in nums[1:]:
            if current > previous:
                previous = current
            else:
                operations += previous + 1 - current
                previous += 1
        return operations


if __name__ == '__main__':
    import Test

    Test.test(Solution().minOperations, [
        ([1, 1, 1], 3),
        ([1, 5, 2, 4, 1], 14),
        ([8], 0),
    ])

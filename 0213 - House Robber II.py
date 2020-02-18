from typing import List


# Dynamic programming. Time: O(n). Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums + [0])
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    # v[n] = max(v[n-2] + v[n], v[n-1])
    def helper(self, nums: List[int]) -> int:
        c1, c2 = nums[0], max(nums[:2])
        for n in nums[2:]:
            c1, c2 = c2, max(c1 + n, c2)
        return c2


if __name__ == '__main__':
    import Test

    Test.test(Solution().rob, [
        ([], 0),
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
    ])

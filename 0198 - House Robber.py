# Dynamic programming. Time: O(n). Space: O(1)
class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums + [0])
        # v[n] = max(v[n-2] + v[n], v[n-1])
        c1, c2 = nums[0], max(nums[:2])
        for n in nums[2:]:
            c1, c2 = c2, max(c1 + n, c2)
        return c2


if __name__ == '__main__':
    import Test

    Test.test(Solution().rob, [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 1, 2, 1, 2], 6),
        ([3, 3, 2, 1], 5),
        ([1, 20, 3, 4, 15, 6], 35),
        ([2, 1, 1, 2], 4),
        ([0, 1, 0], 1),
    ])

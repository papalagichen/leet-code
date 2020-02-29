from typing import List


# Backtracking. Time: O(n^2). Space: O(n^2)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, len(nums))

    def helper(self, nums: List[int], n: int) -> List[List[int]]:
        results = [[]]
        for i in range(len(nums)):
            for x in self.helper(nums[i + 1:], n - 1):
                results.append([nums[i]] + x)
        return results


if __name__ == '__main__':
    import Test

    Test.test(Solution().subsets, [
        ([1, 2], [
            [],
            [1],
            [2],
            [1, 2]
        ]),
        ([1, 2, 3], [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]),
    ], sort_result=True)

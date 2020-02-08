from typing import List


# Recursive. Time: O(n!). Space: O(1)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        if len(nums) == 1:
            results.append(nums)
        for i in range(len(nums)):
            for r in self.permute(nums[:i] + nums[i + 1:]):
                results.append([nums[i]] + r)
        return results


# Backtracking. Time: O(n!). Space: O(1)
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0)

    def helper(self, nums: List[int], left: int) -> List[List[int]]:
        results = []
        if left == len(nums) - 1:
            results.append(nums.copy())
        else:
            for i in range(left, len(nums)):
                nums[left], nums[i] = nums[i], nums[left]
                results.extend(self.helper(nums, left + 1))
                nums[left], nums[i] = nums[i], nums[left]
        return results


if __name__ == '__main__':
    import Test

    Test.test([Solution().permute, Solution2().permute], [
        ([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
        ]),
    ], sort_result=True)

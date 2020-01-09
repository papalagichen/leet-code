from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(t) for t in set(tuple(p) for p in self.helper(nums))]

    def helper(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        results = []
        for i in range(len(nums)):
            for result in self.helper(nums[:i] + nums[i + 1:]):
                results.append([nums[i]] + result)
        return results


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(sorted(nums))

    def helper(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        results = []
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                continue
            for result in self.helper(nums[:i] + nums[i + 1:]):
                results.append([nums[i]] + result)
        return results


if __name__ == '__main__':
    import Test

    Test.test([Solution().permuteUnique, Solution2().permuteUnique], [
        ([1, 1, 2], [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ]),
    ], sort_result=True)

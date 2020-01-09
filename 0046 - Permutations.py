from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.p(nums, 0, results)
        return results

    def p(self, nums: List[int], left: int, results: List[List[int]]):
        if left == len(nums) - 1:
            results.append(nums.copy())
        else:
            for i in range(left, len(nums)):
                nums[left], nums[i] = nums[i], nums[left]
                self.p(nums, left + 1, results)
                nums[left], nums[i] = nums[i], nums[left]


if __name__ == '__main__':
    import Test

    Test.test(Solution().permute, [
        ([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2],
        ]),
    ])

from typing import List

"""
   2 3  -2   4
 2 4 6 -12 -48
 3   3  -6 -24
-2      -2  -8
 4           4

max_product(i) = max(max_product(i - 1), nums[i] * product(i - 1))
 
    2 3  -2   4
min 2 3 -12 -48
max 2 6  -2   4
 
    2 3  -2  -4
min 2 3 -12  -4
max 2 6  -2  48

    2 3 0 4 -1
min 2 3 0 0 -4
max 2 6 0 4 -1

Need to keep max and min for every step
"""


# Dynamic Programming. Time: O(n^2). Space: O(n^2)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mem = [[0] * len(nums) for _ in range(len(nums))]
        max_product = nums[0]
        for i in range(len(nums)):
            mem[i][i] = nums[i]
            max_product = max(max_product, mem[i][i])
            for j in range(i + 1, len(nums)):
                mem[i][j] = mem[i][j - 1] * nums[j]
                max_product = max(max_product, mem[i][j])
        return max_product


# Dynamic Programming. Time: O(n^2). Space: O(1)
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        for i in range(len(nums)):
            mem = nums[i]
            max_product = max(max_product, mem)
            for j in range(i + 1, len(nums)):
                mem *= nums[j]
                max_product = max(max_product, mem)
        return max_product


# Dynamic Programming. Time: O(n). Space: O(1)
class Solution3:
    def maxProduct(self, nums: List[int]) -> int:
        result, max_product, min_product = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_product *= nums[i]
            min_product *= nums[i]
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            max_product = max(max_product, nums[i])
            min_product = min(min_product, nums[i])
            result = max(result, max_product)
        return result


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxProduct, Solution2().maxProduct, Solution3().maxProduct], [
        ([1], 1),
        ([2, 3, -2, 4], 6),
        ([2, 3, -2, -4], 48),
        ([-2, 0, -1], 0),
        ([0, 2], 2),
        ([-5, 2, 4, 1, -2, 2, -6, 3, -1, -1, -1, -2, -3, 5, 1, -3, -4, 2, -4, 6, -1, 5, -6, 1, -1, -1, 1, 1, -1, 1, 1,
          -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1,
          -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1,
          1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1,
          1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1,
          -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1,
          -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1,
          1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1,
          1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1,
          1, -1, -1, -1, -1, -1, -1], 1492992000)
    ])

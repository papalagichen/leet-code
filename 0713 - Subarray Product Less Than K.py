from typing import List


# Dynamic programming. Time: O(n^2)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        products = []
        result = 0
        for n in nums:
            new_products = []
            for p in products + [1]:
                if p * n < k:
                    new_products.append(p * n)
                    result += 1
            products = new_products
        return result


# Sliding window. Time: O(n). Space: O(1)
class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        result = 0
        product = 1
        for i, n in enumerate(nums):
            product *= n
            while product >= k and start <= i:
                product /= nums[start]
                start += 1
            result += i - start + 1
        return result


if __name__ == '__main__':
    import Test

    Test.test([Solution().numSubarrayProductLessThanK, Solution2().numSubarrayProductLessThanK], [
        (([10, 5, 2, 6], 100), 8),
        (([1, 1, 1, 1, 1], 2), 15),
        (([1, 2, 3], 0), 0),
    ])

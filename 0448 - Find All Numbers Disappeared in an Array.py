from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            n = nums[i]
            while nums[n - 1] != n:
                m = n
                n, nums[m - 1] = nums[n - 1], m
        a = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                a.append(i + 1)
        return a

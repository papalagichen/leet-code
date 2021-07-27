import bisect
from typing import List

"""
10 9 2 5 3 7 101 18
-------------------
1
   1
     1
       2
         2
           3
             4
                 4
"""


# Dynamic Programming. Time O(n^2). Space O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        mem = [0] * len(nums)
        for i in range(len(nums)):
            mem[i] = self.look_back(nums[i], nums[:i + 1], mem) + 1
        return max(mem)

    def look_back(self, target: int, nums: List[int], mem: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            if nums[i] < target:
                max_length = max(max_length, mem[i])
        return max_length


# Dynamic Programming + Binary Search. Time O(n lg n). Space O(n)
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        mem = []
        for n in nums:
            i = bisect.bisect_left(mem, n)
            if i >= len(mem):
                mem.append(n)
            else:
                mem[i] = n
        return len(mem)


if __name__ == '__main__':
    import Test

    Test.test((Solution().lengthOfLIS, Solution2().lengthOfLIS), [
        (([1, 2, 3]), 3),
        (([1, 1, 1]), 1),
        (([10, 9, 2, 5, 3, 7, 101, 18]), 4),
        (([-2, -1]), 2),
        (([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6),
    ])

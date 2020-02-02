from typing import List
from typing import Tuple


# Dynamic programming with time O(n^2) and space O(n)
# Reference 0300 - Longest Common Subsequence
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        mem = [0] * len(nums)
        mem2 = [0] * len(nums)

        for i in range(len(nums)):
            mem[i] = self.look_back(nums[i], nums[:i + 1], mem) + 1

            if mem[i] == 1:
                mem2[i] = 1
            else:
                for j in range(i):
                    if mem[j] == mem[i] - 1 and nums[j] < nums[i]:
                        mem2[i] += mem2[j]

        max_length = max(mem)
        total = 0

        for i in range(len(mem)):
            if mem[i] == max_length:
                total += mem2[i]

        return total

    def look_back(self, target: int, nums: List[int], mem: List[int]) -> int:
        max_length = 0

        for i in range(len(nums)):
            if nums[i] < target:
                max_length = max(max_length, mem[i])

        return max_length


class Solution2:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        mem = [0] * len(nums)
        mem2 = [0] * len(nums)

        for i in range(len(nums)):
            mem[i], mem2[i] = self.look_back(nums[i], nums[:i + 1], mem, mem2) + 1

        return max(mem2)

    def look_back(self, target: int, nums: List[int], mem: List[int], mem2: List[int]) -> Tuple[int, int]:
        max_length = 0
        x = 0

        for i in range(len(nums)):
            if nums[i] < target:
                if mem[i] > max_length:
                    max_length = mem[i]
                    x = []

        return max_length, prev_max


if __name__ == '__main__':
    import Test

    Test.test([Solution().findNumberOfLIS, ], [
        ([1, 3, 5, 4, 7], 2),
        ([2, 2, 2, 2, 2], 5),
        ([2, 2, 3, 1, 2], 3),
        ([2, 2, 3, 1, 2, 3], 1),
        ([1, 2, 4, 3, 5, 4, 7, 2], 3)
    ])

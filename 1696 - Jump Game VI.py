from collections import deque
from typing import List

"""
        1 -1 -2  4 -7 3, 2
max_sum 1  0 -1  4 -3 7   

        10 -5 -2  4  0  3, 3
max_sum 10  5  8 14 14 17

maxResult(i) = nums[i] + max(maxResult(i-1) .. maxResult(i-k))
maxResult(i-1) = nums[i-1] + max(maxResult(i-2) .. maxResult(i-k))
"""


# Brute Force. Time: O(n * k). Space: O(n)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        max_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            max_sum[i] = nums[i] + max(max_sum[i - k if i - k > 0 else 0:i])
        return max_sum[-1]


# Dynamic Programming. Time: O(n). Space: O(1)
class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        max_sums = [0] * len(nums)
        max_sums[0] = nums[0]
        q = deque([(nums[0], 0)])  # (sum, index)
        for i in range(1, len(nums)):
            if len(q) > 0 and q[0][1] < i - k:
                q.popleft()
            max_sums[i] = q[0][0] + nums[i]
            while len(q) > 0 and q[-1][0] < max_sums[i]:
                q.pop()
            q.append((max_sums[i], i))
        return max_sums[-1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxResult, Solution2().maxResult], [
        (([1, -1, -2, 4, -7, 3], 2), 7),
        (([10, -5, -2, 4, 0, 3], 3), 17),
    ])

from collections import deque
from typing import List

"""
Priority Queue. Time: O(n lg n). Space: O(k) 
[1, 3, -1, -3, 5, 3, 6, 7], 3
 --------                      (3, 1, -1)   3
    ---------                  (3, -1, -3)  3
       ---------               (5, -3, -1)  5
           --------            (5, 3, -3)   5
               -------         (5, 3, 6)    6
                  -------      (7, 6, 5)    7

Max Sliding Window. Time: O(n). Space: O(k). At each step the head of the deque is the max element in [i-(k-1),i]                   
[1, 3, -1, -3, 5, 3, 6, 7], 3
 -                             (0)
 ----                          (1)
 --------                      (1, 2)     3
    ---------                  (1, 2, 3)  3
       ---------               (4)        5
           --------            (4, 5)     5
               -------         (6)        6
                  --------     (7)        7
"""


# Max Sliding Window. Time: O(n). Space: O(k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_windows = []
        q = deque()
        for i in range(len(nums)):
            if len(q) > 0 and q[0] < i - k + 1:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i + 1 >= k:
                max_windows.append(nums[q[0]])
        return max_windows


if __name__ == '__main__':
    import Test

    Test.test(Solution().maxSlidingWindow, [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1], 1), [1]),
        (([1, -1], 1), [1, -1]),
        (([9, 11], 2), [11]),
        (([4, -2], 2), [4]),
    ])

from typing import List

"""
1 2 3 4 5 6 1
-----           6
        -----  12*
---         -   4
-         ---   8

1 2 3 4 5 6 1 1 2 3 4 5 6 1
        -----------
"""


# Sliding Window. Time: O(n). Space: O(n)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        nums = cardPoints[-k:] + cardPoints[:k]
        score = sum(nums[:k])
        max_score = score
        for i in range(k, len(nums)):
            score += nums[i] - nums[i - k]
            max_score = max(max_score, score)
        return max_score


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxScore], [
        (([1], 1), 1),
        (([1, 2, 3, 4, 5, 6, 1], 3), 12),
        (([2, 2, 2], 2), 4),
        (([9, 7, 7, 9, 7, 7, 9], 7), 55),
        (([1, 1000, 1], 1), 1),
        (([1, 79, 80, 1, 1, 1, 200, 1], 3), 202),
    ])

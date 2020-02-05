from typing import List


# Calculate intersection. Make sure intersection coordinates stay positive
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a1 = (max(rec1[0], rec2[0]), max(rec1[1], rec2[1]))
        a2 = (min(rec1[2], rec2[2]), min(rec1[3], rec2[3]))
        return a2[0] - a1[0] > 0 and a2[1] - a1[1] > 0


# Compare coordinates
class Solution2:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec2[2] > rec1[0] and rec2[3] > rec1[1]


if __name__ == '__main__':
    import Test

    Test.test([Solution().isRectangleOverlap, Solution2().isRectangleOverlap], [
        (([0, 0, 2, 2], [1, 1, 3, 3]), True),
        (([0, 0, 1, 1], [1, 0, 2, 1]), False),
        (([7, 8, 13, 15], [10, 8, 12, 20]), True),
        (([5, 15, 8, 18], [0, 3, 7, 9]), False),
    ])

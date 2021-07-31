from typing import List

"""
110
1's indices = 0, 1
Each operation at position is the sum of each 1's indices - current index
"""


# Time: O(n^2). Space: O(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices = [i for i in range(len(boxes)) if boxes[i] == '1']
        return [sum(abs(x - i) for x in indices) for i in range(len(boxes))]


if __name__ == '__main__':
    import Test

    Test.test(Solution().minOperations, [
        ('110', [1, 1, 3]),
        ('001011', [11, 8, 5, 4, 3, 4]),
    ])

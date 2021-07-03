from typing import List

"""
4 2 3 0 3 1 2
          *
        *   *
  *
      *
"""


# Dynamic Programming. Time: O(n). Space: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.helper(arr, start, [False] * len(arr))

    def helper(self, arr: List[int], start: int, mem: List[int]) -> bool:
        can_forward = can_backward = False
        forward = start + arr[start]
        if forward < len(arr):
            if arr[forward] == 0:
                return True
            if mem[forward] is False:
                mem[forward] = True
                can_forward = self.helper(arr, forward, mem)
        backward = start - arr[start]
        if backward >= 0:
            if arr[backward] == 0:
                return True
            if mem[backward] is False:
                mem[backward] = True
                can_backward = self.helper(arr, backward, mem)
        return can_forward or can_backward


# Dynamic Programming. Time: O(n). Space: O(1)
class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False


if __name__ == '__main__':
    import Test

    Test.test([Solution().canReach, Solution2().canReach], [
        (([0], 0), True),
        (([0, 1], 0), True),
        (([0, 1], 1), True),
        (([4, 2, 3, 0, 3, 1, 2], 5), True),
        (([4, 2, 3, 0, 3, 1, 2], 0), True),
        (([3, 0, 2, 1, 2], 2), False),
        (([47, 26, 216, 78, 179, 101, 42, 233, 185, 56, 303, 310, 169, 338, 51, 104, 308, 162, 81, 82, 169, 41,
           106, 150, 285, 298, 33, 251, 289, 236, 256, 227, 197, 186, 267, 326, 268, 243, 89, 347, 72, 0, 89, 157,
           90, 333, 327, 76, 106, 68, 355, 124, 234, 70, 43, 248, 259, 280, 199, 201, 312, 327, 217, 278, 330,
           258, 348, 351, 223, 240, 143, 244, 64, 343, 339, 101, 193, 18, 140, 312, 71, 225, 111, 79, 199, 226,
           321, 344, 31, 177, 362, 115, 341, 79, 146, 303, 348, 291, 250, 169, 78, 307, 325, 33, 338, 316, 201,
           343, 37, 37, 0, 15, 341, 38, 44, 67, 280, 128, 31, 106, 220, 172, 349, 142, 339, 181, 102, 351, 81,
           209, 41, 181, 59, 216, 230, 170, 257, 52, 5, 338, 28, 75, 208, 307, 108, 103, 34, 342, 82, 233, 263,
           12, 167, 358, 316, 150, 337, 158, 78, 231, 26, 22, 147, 81, 12, 319, 161, 12, 75, 129, 54, 119, 131,
           334, 292, 253, 255, 98, 39, 67, 146, 15, 329, 120, 80, 347, 89, 124, 303, 315, 235, 55, 1, 100, 290,
           187, 333, 326, 87, 138, 48, 41, 153, 118, 192, 152, 279, 69, 154, 71, 152, 273, 61, 153, 267, 51, 106,
           225, 204, 327, 50, 15, 202, 244, 328, 3, 150, 355, 240, 240, 188, 92, 107, 244, 280, 102, 265, 273,
           328, 115, 70, 221, 357, 101, 186, 251, 116, 24, 125, 58, 185, 34, 356, 21, 108, 221, 169, 208, 230,
           226, 235, 336, 304, 315, 334, 329, 229, 190, 20, 104, 348, 132, 66, 265, 55, 212, 102, 167, 52, 2, 328,
           114, 101, 196, 99, 155, 158, 337, 191, 119, 14, 347, 127, 305, 142, 156, 92, 340, 358, 58, 7, 178, 79,
           355, 289, 199, 251, 233, 351, 57, 115, 306, 179, 31, 42, 123, 87, 101, 218, 71, 193, 205, 300, 180, 42,
           19, 280, 233, 293, 181, 147, 359, 190, 168, 191, 5, 58, 198, 154, 139, 29, 342, 261, 245, 141, 26, 251,
           162, 360, 219, 233, 297, 287, 262, 112, 87, 261, 21, 205, 131, 98, 161, 103, 57], 313), True),
    ])

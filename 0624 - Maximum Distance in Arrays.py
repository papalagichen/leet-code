from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arrays = sorted(arrays, key=lambda x: x[0])
        max_arrays = sorted(arrays, key=lambda x: x[-1])
        if min_arrays[0] is max_arrays[-1]:
            return max(abs(min_arrays[0][0] - max_arrays[-2][-1]),
                       abs(min_arrays[1][0] - max_arrays[-1][-1]))
        else:
            return abs(min_arrays[0][0] - max_arrays[-1][-1])


class Solution2:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min, global_max = arrays[0][0], arrays[0][-1]
        max_distance = 0
        for array in arrays[1:]:
            max_distance = max(max_distance, abs(array[0] - global_max), abs(array[-1] - global_min))
            global_min = min(global_min, array[0])
            global_max = max(global_max, array[-1])
        return max_distance


if __name__ == '__main__':
    import Test

    Test.test([Solution().maxDistance, Solution2().maxDistance], [
        (
            [
                [1, 2, 3],
                [4, 5],
                [1, 2, 3]
            ], 4
        ),
        (
            [
                [1],
                [1]
            ], 0
        ),
        (
            [
                [-2],
                [-3, -2, 1]
            ], 3
        )
    ])

import bisect
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mem = []

        for interval in intervals:
            i0 = interval[0]
            c0 = bisect.bisect_left(mem, i0)

            i1 = interval[1]
            c1 = bisect.bisect_right(mem, i1)

            if c0 % 2 == 0 and c1 % 2 == 0:
                mem = mem[:c0] + [i0, i1] + mem[c1:]
            elif c0 % 2 == 0 and c1 % 2 == 1:
                mem = mem[:c0] + [i0] + mem[c1:]
            elif c0 % 2 == 1 and c1 % 2 == 0:
                mem = mem[:c0] + [i1] + mem[c1:]
            elif c0 % 2 == 1 and c1 % 2 == 1:
                mem = mem[:c0] + mem[c1:]

        return [[mem[i], mem[i + 1]] for i in range(0, len(mem), 2)]

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        results = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            if current[1] < intervals[i][0]:
                results.append(current)
                current = intervals[i]
            else:
                current = [min(current[0], intervals[i][0]), max(current[1], intervals[i][1])]
        results.append(current)
        return results

    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if len(results) > 0 and results[-1][1] >= interval[0]:
                results[-1][1] = max(results[-1][1], interval[1])
            else:
                results.append(interval)
        return results


if __name__ == '__main__':
    import Test

    Test.test([Solution().merge, Solution().merge2, Solution().merge3], [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]]
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]]
        ),
        (
            [[1, 4], [5, 10]],
            [[1, 4], [5, 10]]
        ),
        (
            [[1, 3], [5, 7], [9, 11], [2, 10]],
            [[1, 11]]
        ),
        (
            [[1, 3], [5, 7], [9, 11], [4, 8]],
            [[1, 3], [4, 8], [9, 11]]
        ),
        (
            [[1, 3], [5, 7], [9, 11], [3, 9]],
            [[1, 11]]
        ),
        (
            [[1, 4], [0, 0]],
            [[0, 0], [1, 4]]
        )
    ])

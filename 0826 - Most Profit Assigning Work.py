from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = 0
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        i, j = 0, 0
        best = 0
        while i < len(jobs) and j < len(worker):
            if worker[j] < jobs[i][0]:
                max_profit += best
                j += 1
            else:
                best = max(best, jobs[i][1])
                i += 1
        return max_profit + best * (len(worker) - j)


if __name__ == '__main__':
    import Test

    Test.test(Solution().maxProfitAssignment, [
        (([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]), 100),
        (([85, 47, 57], [24, 66, 99], [40, 25, 25]), 0),
        (([68, 35, 52, 47, 86], [67, 17, 1, 81, 3], [92, 10, 85, 84, 82]), 324),
        ((
             [66, 1, 28, 73, 53, 35, 45, 60, 100, 44, 59, 94, 27, 88, 7, 18, 83, 18, 72, 63],
             [66, 20, 84, 81, 56, 40, 37, 82, 53, 45, 43, 96, 67, 27, 12, 54, 98, 19, 47, 77],
             [61, 33, 68, 38, 63, 45, 1, 10, 53, 23, 66, 70, 14, 51, 94, 18, 28, 78, 100, 16],
         ), 1392),
    ])

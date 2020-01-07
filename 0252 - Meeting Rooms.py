import bisect
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        meetings = []
        for interval in intervals:
            c0 = bisect.bisect_right(meetings, interval[0])
            c1 = bisect.bisect_left(meetings, interval[1])
            if c0 % 2 == 1 or c1 % 2 == 1 or abs(c0 - c1) > 1:
                return False
            meetings.insert(c0, interval[0])
            meetings.insert(c0 + 1, interval[1])
        return True

    def canAttendMeetings2(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


if __name__ == '__main__':
    import Test

    Test.test([Solution().canAttendMeetings, Solution().canAttendMeetings2], [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([[17, 20], [17, 20]], False),
        ([[1, 2], [2, 3]], True),
        ([[9, 10], [4, 9], [4, 17]], False),
        ([[12, 13], [6, 11], [2, 19]], False),
    ])

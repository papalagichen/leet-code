from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            for room in rooms:
                if room[-1][1] <= interval[0]:
                    room.append(interval)
                    break
            else:
                rooms.append([interval])
        return len(rooms)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        rooms = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            for i in range(len(rooms)):
                if rooms[i][1] <= interval[0]:
                    rooms[i] = interval
                    break
            else:
                rooms.append(interval)
        return len(rooms)


if __name__ == '__main__':
    import Test

    Test.test([Solution().minMeetingRooms, Solution().minMeetingRooms2], [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[7, 10]], 1),
    ])

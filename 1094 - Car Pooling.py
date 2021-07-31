from typing import List

"""
1 2 3 4 5 6 7 8 9
2--------
    3--------
2 2 5 5 5 3        4 False    
    
2--------
    3--------
2 2 5 5 5 3        5 True

2--------
        3----
2 2 2 2 3 3        3 True

  3----------
            3----
    8------------ 
  3 11 11 11 11 11 11 True
"""


# Brute Force. Time: O(n^2). Space: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1000
        for trip in trips:
            for i in range(trip[1], trip[2]):
                stops[i] += trip[0]
                if stops[i] > capacity:
                    return False
        return True


# Brute Force. Time: O(n). Space: O(n)
class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mem = {}
        for t in trips:
            n, i, j = t
            mem[i] = mem.get(i, 0) + n
            mem[j] = mem.get(j, 0) - n
        for k in sorted(mem.keys()):
            capacity -= mem[k]
            if capacity < 0:
                return False
        return True


if __name__ == '__main__':
    import Test

    Test.test([Solution().carPooling, Solution2().carPooling], [
        (([[2, 1, 5], [3, 3, 7]], 4), False),
        (([[2, 1, 5], [3, 3, 7]], 5), True),
        (([[2, 1, 5], [3, 5, 7]], 3), True),
        (([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11), True),
    ])

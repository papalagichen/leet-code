from typing import List, Dict

"""    0 1  5 3  max
10     1 1  4 2   4
0001   3 1  1 1   3
111001 2 4  - -   2
1      0 1  1 0   2
0      1 0  0 0   1

       0 1  1 1  max
10     1 1  0 0   2
 0     1 0  0 1   2
 1     0 1  0 0   1
"""


# Brute Force. Time: O(n^2). Space: (1)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        a = 0
        if m >= strs[0].count('0') and n >= strs[0].count('1'):
            a = 1 + self.findMaxForm(strs[1:], m - strs[0].count('0'), n - strs[0].count('1'))
        return max(a, self.findMaxForm(strs[1:], m, n))


# Dynamic Programming Recursive Version. Time: O(n). Space: O(n^3)
class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.helper(strs, 0, m, n, dict())

    def helper(self, strs: List[str], index: int, m: int, n: int, mem: Dict) -> int:
        if index == len(strs) or m == 0 and n == 0:
            return 0
        mem_key = (index, m, n)
        if mem_key in mem:
            return mem[mem_key]
        sub_max = 0
        s = strs[index]
        if m >= s.count('0') and n >= s.count('1'):
            sub_max = 1 + self.helper(strs, index + 1, m - s.count('0'), n - s.count('1'), mem)
        result = max(sub_max, self.helper(strs, index + 1, m, n, mem))
        mem[mem_key] = result
        return result


if __name__ == '__main__':
    import Test

    Test.test([Solution2().findMaxForm], [
        ((["10", "0001", "111001", "1", "0"], 5, 3), 4),
        ((["10", "0", "1"], 1, 1), 2),
        ((["10", "0001", "111001", "1", "0"], 4, 3), 3),
        ((["11", "11", "0", "0", "10", "1", "1", "0", "11", "1", "0", "111", "11111000", "0", "11", "000", "1", "1",
           "0", "00", "1", "101", "001", "000", "0", "00", "0011", "0", "10000"], 90, 66), 29),
        ((["111", "1000", "1000", "1000"], 9, 3), 3),
        ((["1000", "1000", "1000"], 9, 3), 3),
    ])

# https://www.youtube.com/watch?v=qli-JCrSwuk

from typing import Dict


class Solution:
    def num_ways(self, data: str) -> int:
        if data == '':
            return 1
        if data[0] == '0':
            return 0
        ways = 0
        if len(data) >= 1:
            ways += self.num_ways(data[1:])
        if len(data) >= 2 and int(data[:2]) <= ord('z') - ord('a'):
            ways += self.num_ways(data[2:])
        return ways


class Solution2:
    def num_ways(self, data: str) -> int:
        return self.num_ways_mem(data, {})

    def num_ways_mem(self, data: str, mem: Dict[str, int]) -> int:
        if data in mem:
            return mem[data]

        if data == '':
            return 1
        if data[0] == '0':
            return 0

        if len(data) >= 1:
            mem[data] = self.num_ways(data[1:])
        if len(data) >= 2 and int(data[:2]) <= ord('z') - ord('a'):
            mem[data] += self.num_ways(data[2:])
        return mem[data]


if __name__ == '__main__':
    import Test

    Test.test([Solution().num_ways, Solution().num_ways], [
        ("12", 2),
        ("011", 0),
        ("101", 1),
    ])

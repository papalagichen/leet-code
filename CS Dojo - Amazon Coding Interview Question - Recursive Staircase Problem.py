# https://www.youtube.com/watch?v=5o-kdjv7FD0
class Solution:
    def num_ways(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n >= 2:
            return self.num_ways(n - 1) + self.num_ways(n - 2)


class Solution2:
    def num_ways(self, n: int) -> int:
        return self.num_ways_mem(n, {})

    def num_ways_mem(self, n: int, mem: dict) -> int:
        if n in mem:
            return mem[n]

        if n <= 1:
            mem[n] = 1
        else:
            mem[n] = self.num_ways(n - 1) + self.num_ways(n - 2)

        return mem[n]


if __name__ == '__main__':
    import Test

    Test.test([Solution().num_ways, Solution2().num_ways], [
        (4, 5),
    ])

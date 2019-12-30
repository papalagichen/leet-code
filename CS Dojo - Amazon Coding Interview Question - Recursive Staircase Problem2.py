# https://www.youtube.com/watch?v=5o-kdjv7FD0
class Solution:
    def num_ways(self, n: int, x: set) -> int:
        if n <= 1:
            return 1

        return sum(self.num_ways(n - i, x) for i in x if i <= n)


class Solution2:
    def num_ways(self, n: int, x: set) -> int:
        return self.num_ways_mem(n, x, {})

    def num_ways_mem(self, n: int, x: set, mem: dict) -> int:
        if n in mem:
            return mem[n]

        if n <= 1:
            mem[n] = 1
        else:
            mem[n] = sum(self.num_ways_mem(n - i, x, mem) for i in x if i <= n)

        return mem[n]


if __name__ == '__main__':
    import Test

    Test.test([Solution().num_ways, Solution2().num_ways], [
        ((4, {1, 3, 5}), 3),
    ])

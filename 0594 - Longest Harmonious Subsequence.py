from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mem = dict()
        for n in nums:
            mem[n] = 1 + mem.get(n, 0)
        max_length = 0
        for n in sorted(mem.keys()):
            if n + 1 in mem:
                max_length = max(max_length, mem[n] + mem[n + 1])
        return max_length


if __name__ == "__main__":
    import Test

    Test.test(Solution().findLHS, [
        (([1, 3, 2, 2, 5, 2, 3, 7]), 5),
    ])

# https://www.youtube.com/watch?v=nqlNzOcnCfs

from typing import Dict
from typing import Set


class Solution:
    def count_set(self, nums: Set[int], total: int) -> int:
        if total == 0:
            return 1
        if len(nums) == 0:
            return 0
        x = nums.copy()
        n = x.pop()
        return self.count_set(x, total) + self.count_set(x, total - n)


class Solution2:
    def count_set(self, nums: Set[int], total: int) -> int:
        return self.count_set_mem(nums, total, {})

    def count_set_mem(self, nums: Set[int], total: int, mem: Dict[str, int]) -> int:
        if total == 0:
            return 1
        if len(nums) == 0:
            return 0
        key = f"{str(nums)}{total}"
        if key in mem:
            return mem[key]
        x = nums.copy()
        n = x.pop()
        mem[key] = self.count_set(x, total) + self.count_set(x, total - n)
        return mem[key]


if __name__ == '__main__':
    import Test

    Test.test([Solution().count_set, Solution2().count_set], [
        (({2, 4, 6}, 0), 1),
        (({1, 2}, 4), 0),
        (({2, 4, 6, 10}, 16), 2),
    ])
